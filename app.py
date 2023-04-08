from pdf_processing import extract_text_from_pdf, preprocess_text
from gpt_integration import review_paper_gpt3
from post_processing import extract_key_points

def main():
    # Read and preprocess the PDF file
    pdf_path = '/Users/s2222119/Reviewer4/CRISPR.pdf'
    extracted_text = extract_text_from_pdf(pdf_path)
    preprocessed_chunks = preprocess_text(extracted_text)

    # Iterate through the chunks and send them to GPT-3 for review
    with open("output.txt", "a") as output_file:
        for chunk in preprocessed_chunks:
            review = review_paper_gpt3(chunk)

            # Extract key points from the GPT-3 review
            key_points = extract_key_points(review)

            # Write the results to the output file
            output_file.write("Summary:\n")
            output_file.write(key_points["summary"] + "\n")
            output_file.write("Strengths:\n")
            output_file.write(", ".join(key_points["strengths"]) + "\n")
            output_file.write("Weaknesses:\n")
            output_file.write(", ".join(key_points["weaknesses"]) + "\n\n")

            # Print the results
            print("Summary:", key_points["summary"])
            print("Strengths:", ", ".join(key_points["strengths"]))
            print("Weaknesses:", ", ".join(key_points["weaknesses"]))
            print("\n")

if __name__ == "__main__":
    main()
