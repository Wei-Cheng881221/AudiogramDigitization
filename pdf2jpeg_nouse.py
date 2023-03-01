#remember to download the PTA_finish file and put it under /AudiogramDigitization
from pdf2image import convert_from_path
import os
from tqdm import tqdm

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=("PDF to BMP script"
            "for the conversion of audiology reports from PDF to BMP documents."))
    parser.add_argument("-i", "--input", type=str, required=True,
            help=("Path to the audiology report (or directory) to be transform."))
    parser.add_argument("-o", "--output_dir", type=str, required=True,
            help="Path to the directory in which the result is to be saved.")
    parser.add_argument("-t", "--file_type", type=str, required=True,
            help="Type for the output file. Input : bmp, jpg, png")
    args = parser.parse_args()

    if not os.path.isdir(args.output_dir):
        os.mkdir( args.output_dir )

    input_files = []
    if os.path.isfile(args.input):
        input_files += [os.path.abspath(args.input)]
    else:
        input_files += [os.path.join(args.input, filename) for filename in os.listdir(args.input)]

    with tqdm(total=len(input_files)) as pbar:
        for input_file in input_files:
            pbar.set_description(f"{os.path.basename(input_file)}")

            # Store Pdf with convert_from_path function
            images = convert_from_path(input_file, thread_count = 4)
            head_tail = os.path.split(input_file)
            name, _ = os.path.splitext(head_tail[1])

            for i in range(len(images)):

                # Save pages as images in the pdf
                # images[i].save('page'+ str(i) +'.jpg', 'JPEG')
                if args.file_type == 'bmp':
                    images[i].save(args.output_dir + '/' + name + '_page'+ str(i) +'.bmp', 'BMP')
                elif args.file_type == 'jpg':
                    images[i].save(args.output_dir + '/' + name + '_page'+ str(i) +'.jpg', 'JPEG')
                elif args.file_type == 'png':
                    images[i].save(args.output_dir + '/' + name + '_page'+ str(i) +'.png', 'PNG')
                else:
                    raise ValueError('No file type or not supported type!')
                

            pbar.update(1)
