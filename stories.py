"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, id, title, words, text):
        """Create story with id, title, words and template text."""

        self.id = id
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", f'<span class="user_word">{val}</span>')

        return text


# Here's a story to get you started

story_list = [
    Story(
        id='story-1', 
        title='Going To The Doctor',
        words=['adjective', 'place', 'adjective', 'adjective', 'piece_of_clothing', 'body_part', 'body_part', 'body_part', 'adjective', 'noun', 'noun', 'place', 'adjective'],
        text="""Every year, you should go visit the doctor. It is a very {adjective}
        visit. Usually, you have to skip going to {place} to go. Your doctor is usually
        a/an {adjective} man or woman who is wearing a/an {adjective} {piece_of_clothing}.
        They will look at your {body_part}, {body_part}, and {body_part}. Sometimes,
        they can be very {adjective}. Afterwards, they will give you a {noun} and
        a {noun}, and your mom and dad will take to to {place} as a treat. All in all,
        the doctor's office isn't so {adjective}"""
    ),
    Story(
        id='story-2',
        title='Flying To Australia',
        words=['noun', 'number', 'noun', 'food', 'adjective', 'verb', 'job', 'noun', 'adjective', 'verb', 'verb', 'adjective'],
        text="""I decided to go on a vacation to Australia with a {noun}. We got to the
        airport {number} hours early. When we went through security, I got stopped
        because I forgot to take my {noun} out of my pocket. We got some {food} for the
        flight and arrived at the gate. Once we boarded the plane, I was sitting next
        to a very {adjective} man. He spent the entire flight {verb_ending_with_ing}
        and talking about his job doing {job}. Whenever I tried to sleep, he would
        step around me to go to the {noun}. I was so {adjective}. Since I couldn't
        sleep, I decided to {verb} and {verb} instead. Finally, we arrived in
        Australia. All in all, the flight was {adjective}!"""
    ),
    Story(
        id='story-3',
        title='Bats Are So Cool!',
        words=['color', 'adjective', 'time', 'adjective', 'place', 'food', 'food', 'verb', 'noun', 'number'],
        text="""Bats are so cool! They are {color}, {adjective} animals which have
        wings. They like to fly around at {time} which makes some people scared of
        them. But bats are {adjective}, and they don't want to hurt people. I have
        a pet bat that lives in {place}. I like to feed him {food} and {food}. He
        likes to {verb}. I am his favorite person, but he also likes {plural_noun}.
        I want to convice my parents to get me {number} more bats."""
    )
]
