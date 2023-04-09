from pdf_processing import extract_text_from_pdf, preprocess_text
from gpt_integration import review_paper_gpt3
from post_processing import extract_key_points

def main():
    # Read and preprocess the PDF file
    pdf_path = '/Users/s2222119/Reviewer4/CRISPR.pdf'
    extracted_text = extract_text_from_pdf(pdf_path)
    preprocessed_chunks = preprocess_text(extracted_text)

    # Initialize lists for storing all strengths and weaknesses
    all_strengths = []
    all_weaknesses = []

    # Iterate through the chunks and send them to GPT-3 for review
    for chunk in preprocessed_chunks:
        review = review_paper_gpt3(chunk)

        # Extract key points from the GPT-3 review
        key_points = extract_key_points(review)

        # Add the strengths and weaknesses to their respective lists
        all_strengths.extend(key_points["strengths"])
        all_weaknesses.extend(key_points["weaknesses"])

    # Save the results to a text file
    with open("output.txt", "a") as output_file:
        output_file.write("Summary:\n")
        output_file.write(key_points["summary"] + "\n")
        output_file.write("Strengths:\n")
        output_file.write(", ".join(all_strengths) + "\n")
        output_file.write("Weaknesses:\n")
        output_file.write(", ".join(all_weaknesses) + "\n\n")

if __name__ == "__main__":
    main()
