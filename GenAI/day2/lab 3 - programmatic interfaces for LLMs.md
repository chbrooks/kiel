#### Lab 3 - Programmatic Interfaces to LLMs.

For this lab, we'll use Google's [Vertex AI Studio](https://cloud.google.com/vertex-ai?hl=en). 
There are many different platforms and ecosystems for programming LLMs.
Google has a huge suite of AI tools for public use, and lots of documentation, 
which makes them attractive for learning. Getting
everything set up can sometimes be a little annoying, but once you get
that working, they're very effective.

For this lab, we'll use the Gemini 2.0 Flash model. It's smaller and cheaper,
but plenty effective for our needs. You'll need a Gmail account for this.

To start, go [here](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-2.0-flash-001?project=sample-project-295322)
and click on Open Notebook.

Read through the notebook and follow the steps. Along the way you'll need to enable
the Vertex AI API.

There's a fair amount of code, but a big chunk of it is just setup. If you're new
to programming, see if you can figure out how the prompt is sent to the LLM and how the
response is handled.

If you are more experienced, start modifying the code in the tutorial. How do the results
change if you modify the system prompt? What happens when you adjust the safety filters?
Try changing the inputs in the multimodal section.

Now that you've seen this, return to your brainstorming idea. How would this functionality
change things? Are there pieces you'd like to add in?

