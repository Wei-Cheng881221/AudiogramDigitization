#remember to download the PTA_finish file and put it under /AudiogramDigitization
import os
import fitz
from tqdm import tqdm

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=("PDF to BMP script"
            "for the conversion of audiology reports from PDF to BMP documents."))
    parser.add_argument("-i", "--input", type=str, required=True,
            help=("Path to the audiology report (or directory) to be transform."))
    parser.add_argument("-o", "--output_dir", type=str, required=True,
            help="Path to the directory in which the result is to be saved.")
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
            head_tail = os.path.split(input_file)
            name, _ = os.path.splitext(head_tail[1])
            pdf = fitz.open(input_file)
            for pg in range(len(pdf)):
                page = pdf[pg]
                trans = fitz.Matrix(1.5, 1.5) #調整到跟原始大小相近一點
                pm = page.get_pixmap(matrix=trans)
                pm.save(args.output_dir + '/' + name + "_page"+str(pg+1)+".jpg")
            pdf.close()

            pbar.update(1)
