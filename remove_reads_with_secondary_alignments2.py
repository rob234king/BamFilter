import pysam
import argparse

def filter_bam(input_bam_path, output_bam_path):
    # Open the input BAM file for reading
    input_bam = pysam.AlignmentFile(input_bam_path, 'rb')

    # Create a set to store read names with secondary alignments
    reads_with_secondary = set()

    # Iterate through the BAM file and identify reads with secondary alignments
    for read in input_bam:
        if read.is_secondary:
            reads_with_secondary.add(read.query_name)

    # Close the input BAM file
    input_bam.close()

    # Open the input BAM file again for reading
    input_bam = pysam.AlignmentFile(input_bam_path, 'rb')

    # Create an output BAM file for writing
    output_bam = pysam.AlignmentFile(output_bam_path, 'wb', template=input_bam)

    # Iterate through the BAM file and write only the reads without secondary alignments
    print(reads_with_secondary)
    for read in input_bam:
        
        if read.query_name not in reads_with_secondary:
            output_bam.write(read)

    # Close both the input and output BAM files
    input_bam.close()
    output_bam.close()

    print("Filtered BAM file saved to:", output_bam_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter BAM file to remove reads with secondary alignments")
    parser.add_argument("input_bam_path", help="Path to the input BAM file")
    parser.add_argument("output_bam_path", help="Path for the output BAM file")

    args = parser.parse_args()
    filter_bam(args.input_bam_path, args.output_bam_path)
