import json

# Define questions, options, correct answers, and solutions
questions = [
    {
        "questionNumber": 1,
        "questionId": 481221,
        "questionText": "If Δ=|a11 a12 a13 a21 a22 a23 a31 a32 a33| and Aij is the cofactor of aij, then the value of Δ is equal to",
        "options": [
            {"optionNumber": "A", "optionText": "a11A31 + a12A32 + a13A33", "isCorrect": False},
            {"optionNumber": "B", "optionText": "a11A11 + a12A21 + a13A31", "isCorrect": False},
            {"optionNumber": "C", "optionText": "a21A11 + a22A12 + a23A13", "isCorrect": False},
            {"optionNumber": "D", "optionText": "a11A11 + a21A21 + a31A31", "isCorrect": True}
        ],
        "solutionText": "The determinant Δ can be calculated using the formula: Δ = a11A11 + a21A21 + a31A31."
    },
    {
        "questionNumber": 2,
        "questionId": 481222,
        "questionText": "If the matrix [0 -1 3x; 1 y -5; -6 5 0] is skew-symmetric, then 6x + y is equal to",
        "options": [
            {"optionNumber": "A", "optionText": "6", "isCorrect": False},
            {"optionNumber": "B", "optionText": "12", "isCorrect": True},
            {"optionNumber": "C", "optionText": "18", "isCorrect": False},
            {"optionNumber": "D", "optionText": "2", "isCorrect": False}
        ],
        "solutionText": "A skew-symmetric matrix has zeros on its diagonal and negative of its transpose as its own. Here, comparing elements, y = 0 and 3x = 6. So, 6x + y = 12."
    },
    {
        "questionNumber": 3,
        "questionId": 481223,
        "questionText": "If |3 -4; 2 1| = |2x 5; 1 x|, then |x| is equal to",
        "options": [
            {"optionNumber": "A", "optionText": "√(5/2)", "isCorrect": False},
            {"optionNumber": "B", "optionText": "4", "isCorrect": False},
            {"optionNumber": "C", "optionText": "2√2", "isCorrect": True},
            {"optionNumber": "D", "optionText": "2", "isCorrect": False}
        ],
        "solutionText": "The determinant of a 2x2 matrix [a b; c d] is given by |ad - bc|. Here, |3 -4; 2 1| = |2x 5; 1 x|. Solving, we get 11 = 2x^2 - 5, hence x^2 = 8, and |x| = 2√2."
    },
    {
        "questionNumber": 4,
        "questionId": 481224,
        "questionText": "Which of the following statements are true?\nA. A square matrix A is said to be non-singular if |A| = 0\nB. A square matrix A is invertible if and only if A is non-singular matrix.\nC. If elements of a row are multiplied with cofactors of any other row, then their sum is zero.\nD. A is square matrix of order 3 then |Adj.(A)| = |A|^3\nChoose the correct answer from the options given below",
        "options": [
            {"optionNumber": "A", "optionText": "A and C only", "isCorrect": False},
            {"optionNumber": "B", "optionText": "B and C only", "isCorrect": True},
            {"optionNumber": "C", "optionText": "C and D only", "isCorrect": False},
            {"optionNumber": "D", "optionText": "B and D only", "isCorrect": False}
        ],
        "solutionText": "A square matrix A is non-singular if its determinant |A| ≠ 0, so Statement A is false. Statement B is true as a matrix A is invertible if and only if |A| ≠ 0, making it non-singular. Statement C is true, as the sum of products of elements of a row with their cofactors in any other row is equal to the determinant. Statement D is false, as |Adj(A)| = |A|^2 for a square matrix of any order."
    },
    {
        "questionNumber": 5,
        "questionId": 481225,
        "questionText": "The interval in which y = x^2 * e^(2x) is increasing is",
        "options": [
            {"optionNumber": "A", "optionText": "(-∞,-1)", "isCorrect": False},
            {"optionNumber": "B", "optionText": "(-1, ∞)", "isCorrect": False},
            {"optionNumber": "C", "optionText": "(-∞,-1) ∪ (0, ∞)", "isCorrect": True},
            {"optionNumber": "D", "optionText": "(-∞, 0) ∪ (1, ∞)", "isCorrect": False}
        ],
        "solutionText": "To find where y = x^2 * e^(2x) is increasing, we differentiate dy/dx and find its intervals where it's positive. Solving dy/dx = 2xe^(2x)(x+1), we get dy/dx > 0 for x in (-∞,-1) ∪ (0, ∞), hence the function is increasing in these intervals."
    },
    {
        "questionNumber": 6,
        "questionId": 481226,
        "questionText": "If x = t^3, y = t^4, then d^2y/dx^2 at t = 2 is",
        "options": [
            {"optionNumber": "A", "optionText": "8/3", "isCorrect": False},
            {"optionNumber": "B", "optionText": "1/9", "isCorrect": True},
            {"optionNumber": "C", "optionText": "2/9", "isCorrect": False},
            {"optionNumber": "D", "optionText": "9/16", "isCorrect": False}
        ],
        "solutionText": "Given x = t^3, y = t^4, we find dx/dt = 3t^2 and dy/dt = 4t^3. Then, d^2y/dx^2 = d(dy/dx)/dx. Substituting t = 2, we get d^2y/dx^2 = 1/9."
    }
]

# Convert to JSON
json_data = json.dumps(questions, indent=2)

# Output JSON data
print(json_data)
