from math import ceil
import numpy as np
import hashlib
import time
import cv2


def time_encrypt(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        # print(f'time: {t2}')
        print(f'time: {t2}')
        # return t2
        return result

    return wrapper

class Encrypt:
    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.num_channels = 3

    def hashArray(self, array):
        hash = hashlib.sha512(array.tobytes()).hexdigest()

        return hash

    def splitHash(self, hash):
        quarters = len(hash) // 4

        return [hash[i:i + quarters] for i in range(0, len(hash), quarters)]

    def convertToDecimal(self, hashes):
        into_decimal = [int(hash, 16) for hash in hashes]

        return into_decimal

    def transformDecimal(self, converted_hashes):
        transformedHash = []
        for i, decimal in enumerate(converted_hashes):
            if i % 2 == 0:  # Even indices (0, 2)
                transformedHash.append((float(f"0.{decimal}") * 0.43) + 3.57)
            else:  # Odd indices (1, 3)
                # transformedHash.append(decimal * (10 ** (-39)))
                transformedHash.append(float(f"0.{decimal}"))

        return transformedHash

    def rowShuffle(self, image, x0, r):
        x = x0
        x = r * x * (1 - x)
        # rand_indx.append(x)
        for i in range(len(image) - 1, 0, -1):
            j = ceil(i * x)

            image[[i, j]] = image[[j, i]]
            x = r * x * (1 - x)
            # rand_indx.append(j)

        # Reshape back to original dimensions
        shuffled_pixels = image.reshape(self.num_rows, self.num_cols, self.num_channels)

        return shuffled_pixels

    def colShuffle(self, image, x0, r):
        x = x0
        x = r * x * (1 - x)
        # rand_indx.append(x)
        for i in range(len(image) - 1, 0, -1):
            j = ceil(i * x)

            image[:, [i, j]] = image[:, [j, i]]
            x = r * x * (1 - x)
            # rand_indx.append(j)

        # Reshape back to original dimensions
        shuffled_pixels = image.reshape(self.num_rows, self.num_cols, self.num_channels)

        return shuffled_pixels

    def keystream(self, res, x0, r):
        x = x0
        ks = [x0]
        # create keystream
        for i in range(2000 + ((res * 3) - 1)):
            x = r * x * (1 - x)
            ks.append(x)

        # discard first 2000
        del ks[:2000]

        # convert into numpy array
        ks_array = np.array(ks)

        # produce keystream vector
        kv = np.floor(ks_array * 10 ** 16) % 256
        kv = kv.astype(dtype='int16')

        return kv

    def xor(self, a, b):
        return np.bitwise_xor(a, b)

    @time_encrypt
    def readVideo(self, filepath):
        cap = cv2.VideoCapture(filepath)
        result = cv2.VideoWriter('test_encrypt.avi', cv2.VideoWriter_fourcc(*'HFYU'), cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

        # grabbed, frame = cap.read()

        grabbed = True

        count = 1

        length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(length)
        
        while True:
            grabbed, frame = cap.read()

            if not grabbed: 
                print('read done')
                break

            self.num_rows, self.num_cols, self.num_channels = frame.shape

            hashed = self.hashArray(frame)
            splits = self.splitHash(hashed)
            converted = self.convertToDecimal(splits)
            transform = self.transformDecimal(converted)    # [Logmap1 r, Logmap1 x0, Logmap2 r, Logmap2, x0]

            # permutate
            row_permutated = self.rowShuffle(frame, transform[1], transform[0])
            col_permutated = self.colShuffle(row_permutated, transform[1], transform[0])    # final permutation

            flatten = col_permutated.reshape(-1, self.num_channels)

            # create keystream vector
            kv = self.keystream(self.num_rows * self.num_cols, transform[3], transform[2])
            kr, kg, kb = np.array_split(kv, 3)  # split keystream into three
            comb_ks = np.vstack((kb, kg, kr)).T  # this is the 2d array of the keystream

            # diffuse the pixels
            diffuse = self.xor(flatten, comb_ks)

            # reshape the array into a required cv2 format
            diffuse_pixels = diffuse.reshape(self.num_rows, self.num_cols, self.num_channels)

            # to be replaced by a video writers
            # cv2.imwrite('test_vid/test_im_outs/encryptedtest_%d.png' % count, diffuse_pixels, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            result.write(diffuse_pixels)

            count += 1

            

        cap.release()


if __name__ == '__main__':
    v = Encrypt()

    v.readVideo('test_vid/test2.mp4')
