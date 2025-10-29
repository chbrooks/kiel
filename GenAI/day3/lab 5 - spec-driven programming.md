#### Lab 5: Spec-driven programming with LLMs.

This is based off of [this blog post](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/).

You might've found that it's easy to generate simple applications with
an AI tool, but that as the design gets more complex, it's hard to capture 
all the details correctly. This is true in general for software design,
which is why we usually generate a specification before we start
building.

Generating a detailed spec can be a lot of work. You need to
think carefully about what you are and are not trying to do, what is in scope
for the project, what your users might ask for, and other issues.

An LLM can be a really useful brainstorming tool to nail down these ideas.

Let's extend the brainstorming approach from our earlier assignmnent to generate
a spec for ourselves.

Start with this prompt:

```
Ask me one question at a time so we can develop a thorough,
step-by-step spec for this idea. Each question should build
on my previous answers, and our end goal is to have a detailed
specification I can hand off to a developer. Let’s do this
iteratively and dig into every relevant detail. Remember,
only one question at a time. Here’s the idea:
```

If your project idea is solid enough, you can provide this here. If your project is
really big, or you are still working it out, try this with a single
component, or else pick something else first - for example, a
text-based roguelike game that takes place on a spaceship.

As before, the LLM will ask you questions forever. This process is
really helpful in getting you to think about your project more deeply.
It should ask you about implementation choices, extensibility, platforms, and
everything else a developer would need to know. Once you feel like the main
questions have been addressed, or you are getting tired, you can then
ask it to generate a spec for you.

I like this prompt - feel free to tweak it:

```
Now that we’ve wrapped up the brainstorming process, can you compile
our findings into a comprehensive, developer-ready specification?
Include all relevant requirements, architecture choices, data handling
details, error handling strategies, and a testing plan so a developer
can immediately begin implementation.
```

This should generate a fairly long and comprehensive specifications document. You
might exceed the maximum output length for your model; just hit 'continue' to
keep generating output. Copy and paste it to a file when you're done.

We could give this to a developer to work on, but let's see if we can get further.

Many modern LLM-based tools can do what's referred to as reasoning, which allows
the tool to generate step-by-step processes. Claude's Sonnet 4.5 model can do this,
as can DeepSeek R1, ChatGPT's o3 model, and Gemini 2.5.

Pick your favorite reasoning model and give it this prompt. You'll also upload
the spec document as input.

```
Using this spec, draft a detailed, step-by-step blueprint for building this
project. Then, once you have a solid plan, break it down into small, iterative
chunks that build on each other. Look at these chunks and then go another round
to break it into small steps. review the results and make sure that the steps
are small enough to be implemented safely, but big enough to move the project
forward. Iterate until you feel that the steps are right sized for this project.
 From here you should have the foundation to provide a series of prompts for a
 code-generation LLM that will implement each step. Prioritize best practices,
 and incremental progress, ensuring no big jumps in complexity at any stage.
 Make sure that each prompt builds on the previous prompts, and ends with
 wiring things together. There should be no hanging or orphaned code that isn't
 integrated into a previous step. Make sure and separate each prompt section.
 Use markdown. Each prompt should be tagged as text using code tags. The goal
 is to output prompts, but context, etc is important as well.
```

 This will take a while, but will generate a long document with a list of steps and a
 prompt for each one.

 You can then take the prompts and use them in your favorite code generator.
 You can return to Bolt, or try a new tool like Cursor or Claude Code.

 Run each prompt individually and test the results before continuing. The system should
 build a test suite for you; convince yourself that everything is actually
 working and behaving at each step before you move on. This part is really 
important - how do you know that what's generated is correct?

 I've had good success with this approach. It's not perfect, but I can get a prototype
 built pretty quickly.

 You may find places where the generated code does not do what you want. You can:
 - Dig in yourself and try to debug it
 - Ask the tool to help you debug
 - Cut-and-paste the code into a separate LLM and ask it for help.

You might also back up, break the problem into
smaller pieces, and ask the tool to work on those.