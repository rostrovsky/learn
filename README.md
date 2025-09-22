# Learn

Interactive learning tools for studying various topics through flashcards and quizzes.

## Page

The page is available at: **https://rostrovsky.github.io/learn/**

## Features

- **Flashcards**: Study with interactive flashcards that support touch gestures on mobile
- **Quiz Mode**: Test your knowledge with sequential quiz questions
- **Dark Theme**: Toggle between light and dark theme
- **JSON-based**: Load your own learning materials from JSON files
- **Mobile-friendly**: Touch navigation support for flashcards

## Learning Materials

Learning content is stored in JSON format in the `json` directory:

- **Flashcards**: [`json/flashcard/`](./json/flashcard/) - Contains flashcard decks organized by topic
- **Quizzes**: [`json/quiz/`](./json/quiz/) - Contains quiz questions organized by topic

## Preparing JSONs

### Flashcards

Prompt:

````
<your materials here>

---

Convert above knowledge into flashcards JSON similar to below.

```json
{
  "title": "Artificial Intelligence Fundamentals & Generative AI",
  "version": 1,
  "cards": [
    {
      "id": 1,
      "front": "What is Artificial Intelligence (AI)?",
      "back": [
        "A computer system that imitates some aspect of human behavior or capabilities such as recognizing speech, classifying images, translating languages, making decisions, and predicting outcomes."
      ]
    },
    {
      "id": 2,
      "front": "How does Generative AI differ from regular AI?",
      "back": [
        "Regular AI: Primarily imitates specific human behaviors (e.g., speech recognition, image classification, translation).",
        "Generative AI: Focuses on creating original content after being trained on large amounts of information."
      ]
    }
  ]
}
```
````

### Quiz

````
<your materials here>

---

Convert above knowledge into single and multiple choice quiz according to the below example. Provide at least 20 questions.

```json
{
  "title": "Sample Quiz: Basics",
  "version": 1,
  "questions": [
    {
      "id": 1,
      "type": "single",
      "prompt": "Which planet is known as the Red Planet?",
      "choices": [
        { "id": 1, "text": "Venus", "is_correct": false },
        { "id": 2, "text": "Mars", "is_correct": true },
        { "id": 3, "text": "Jupiter", "is_correct": false }
      ],
      "explanation": "Mars appears red due to iron oxide on its surface."
    },
    {
      "id": 2,
      "type": "multiple",
      "prompt": "Select all prime numbers.",
      "choices": [
        { "id": 1, "text": "2", "is_correct": true },
        { "id": 2, "text": "3", "is_correct": true },
        { "id": 3, "text": "4", "is_correct": false },
        { "id": 4, "text": "5", "is_correct": true }
      ],
      "explanation": "A prime number has exactly two divisors: 1 and itself."
    },
    {
      "id": 3,
      "type": "single",
      "prompt": "What is the chemical symbol for water?",
      "choices": [
        { "id": 1, "text": "H2O", "is_correct": true },
        { "id": 2, "text": "O2", "is_correct": false },
        { "id": 3, "text": "CO2", "is_correct": false }
      ],
      "explanation": "Two hydrogen atoms and one oxygen atom."
    }
  ]
}
```
````
