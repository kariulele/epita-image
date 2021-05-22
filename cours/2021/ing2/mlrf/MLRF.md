# MLRF official web page
J. Chazalon
https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/

Last updated on 2020-06-10 at 14:46:28

This page is archived
Content is outdated but kept for reference.

## Welcome to MLRF official web page
This web page is the official web page for the MLRF course taught at EPITA. Students should find listed here (almost) all the resources they need for this course.

Teachers: Joseph Chazalon (lectures + practice), Olivier Ricou (practice), Julie Rivet (practice), Yizi Chen (practice) and Nicolas Boutry (practice).

Teachers will be available online during scheduled sessions (Monday morning and afternoon).
Students must connect to and attend all online sessions.
Students must watch the lectures before the Q/A sessions.

Students’ weekly workflow should be:

Before Monday: watch the lecture (see below for links) and prepare questions.
On Monday morning: attend the Q/A session using Teams.
On Monday afternoon: work on the practice session and join the discussion using Teams.
Before Sunday evening: (for sessions 4, 5 and 6 only) complete the assignment and submit your results using Moodle.
On the next Monday morning (before the Q/A session): Complete the test about previous lecture and practice using Moodle.


## Tools we are using
We will try to use the right tool for the right job. Here are the tools and their job(s).

- This web site: to share files with you
- Teams:
  * for Q/A sessions and practice sessions with teachers
  * for assistance and chat between students themselves
- Moodle:
  * for graded tests
  * to submit results for practice sessions 4, 5 and 6
  * for the final feedback about the course
- email: on rare occasions for important communication about the course

## Setting up a programming environment on your computer
You need to setup a programming environment on your computer to complete this course. We tried to make this as easy as possible.

We use Jupyter, a notebook interface for scientific Python. We provide you with notebooks that you have to edit to complete each practice session.

To get a working environment, you first need to install a recent (3.5+) Python environment. Then, you need to install some packages to get all the necessary tools We recommend using `pip`, the Python package installer, as follows;

```
pip install --user \
    jupyter \
    matplotlib \
    numpy \
    opencv-contrib-python-headless \
    scikit-image \
    scikit-learn
```

You may need to edit your `$PATH` and add `$HOME/.local/bin` to the list of paths.

Then, you should be able to navigate to a directory containing Jupyter Notebooks (`.ipynb` files) and start a Jupyter server using

`jupyter notebook`

This should automatically launch a browser and let you interact with notebooks. We recommend that you read those two resources to get Jupyter’s basics:

Jupyter Documentation - Running the Notebook (https://jupyter.readthedocs.io/en/latest/running.html)
Jupyter Notebook Overview (https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

## Resources

### Week 1: April 27th
- Lecture 01: Course introduction, Template Matching, Global image descriptors
  * Part 01: Introduction: slides, video
  * Part 02: Course outline: slides, video
  * Part 03 + 04: Intro to Twin it! and Template matching: slides, video
- Practice 01: Introduction to image processing with Python, template matching
  * Student notebooks (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_01_student.tar.gz)
  * Resource files: check private chat on Teams.
  * Solutions (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_01_teacher.tar.gz)

## Week 2: May 4th
- Test 01: Start on 2020-05-04 at 11:00 on Moodle
- Lecture 02: Global and local image descriptors, pattern descriptors, keypoint detectors
  * Part 01: Introduction slides, video
  * Part 02: Global image descriptors slides, video
  * Part 03: Clustering slides, video
  * Part 04: Local feature detectors slides, video
- Practice 02: Color histograms, Harris corner detection, descriptor extraction and matching
  * Student notebooks (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_02_student.tar.gz)
  * Resource files: UPDATED, SAME LINK check private chat on Teams and please re-download.
  * Solutions (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_02_teacher.tar.gz)

## Week 3: May 11th
- Test 02: Start on 2020-05-11 at 11:00 on Moodle
- Lecture 03: Local feature detectors and descriptors, Matching descriptors, Perspective transform estimation
  * Part 01: Introduction slides, video
  * Part 02: Local feature descriptors slides, video
  * Part 03: Descriptor matching and indexing slides, video
  * Part 04: Projective transformations slides, video
  * Part 05: Homography estimation and Geometric validation slides, video
- Practice 03: Augmented Documents
  * Student notebooks (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_03_student.tar.gz)
  * Resource files are included in the archive.
  * Solutions (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_03_teacher.tar.gz)

## Week 4: May 18th
- Test 03: Start on 2020-05-18 at 11:00 on Moodle
- Lecture 04: Content based image retrieval and Evaluation
  * Part 01: Introduction slides video
  * Part 02: CBIR slides video
  * Part 03: Evaluation slides video
  * Part 04: Texture descriptors slides video
  * Part 05: Character descriptors slides video
- Practice 04: Image search engine
  * Student notebooks (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_04_student.tar.gz)
  * Resource files: check private chat on Teams.
  * Result submission form - Deadline: 2020-05-24 at 23:59

## Week 5: May 25th
- Test 04: Start on 2020-05-25 at 11:00 on Moodle
- Lecture 05: Image classification and Evaluation
  * Part 01: Introduction slides video
  * Part 02: Image classification overview slides video
  * Part 03: Some classifiers, part 1 slides video
  * Part 04: Classifier evaluation slides video
- Practice 05: Muffin vs Chihuahua
  * Student notebooks (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_05_student.tar.gz)
  * Resource files: check private chat on Teams.
  * Result submission form - Deadline: 2020-05-31 at 23:59

## Week 6: June 1st
- Test 05: Start on 2020-06-01 at 11:00 on Moodle
- Lecture 06: Image classification, Image Segmentation, Research problems, Conclusions
  * Part 01: Introduction slides video
  * Part 02: Some classifiers, part 2 slides video
  * Part 03: More theory about classification slides video
  * Part 04: Introduction to practice session 6 slides video
  * Part 05: Conclusions slides video
- Practice 06: Brain tumor segmentation
  * Student notebooks (https://www.lrde.epita.fr/~jchazalo/teaching/MLRF/202004_IMAGE_S8_SCIA_S8/practice_06_student.tar.gz)
  * Resource files: check private chat on Teams.
  * Result submission form - Deadline: 2020-06-07 at 23:59

## Week 7: June 8th
- Test 06: Start on 2020-06-09 at 11:00 on Moodle
- Course anonymous feedback form: fill it on Moodle on 2020-06-09
