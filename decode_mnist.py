from PIL import Image
import struct


def read_image(filename):
    f = open(filename,'rb')
    index = 0
    buf = f.read()
    f.close()
    magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
    index += struct.calcsize('>IIII')

    for i in range(images):
        image = Image.new('L', (columns, rows))
        for x in range(rows):
            for y in range(columns):
                image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                index += struct.calcsize('>B')

        print('save ' + str(i) + 'image')
        image.save('D:' + str(i) + '.png')




if __name__ == '__main__':
     read_image('D:\cat-and-dog\\user-images-ubyte')