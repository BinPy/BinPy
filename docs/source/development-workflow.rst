======================
 Development workflow
======================

.. contents::
..
    1  Introduction
    2  How to send a Pull Request
    3  Coding conventions in BinPy
      3.1  Standard Python coding conventions
      3.2  Documentation strings
      3.3  Python 3
    4  Workflow process
      4.1  Create your environment
        4.1.1  Install git
        4.1.2  Install other software
        4.1.3  Basic git settings
        4.1.4  Advanced tuning
        4.1.5  Create GitHub account
        4.1.6  Cloning BinPy
      4.2  Create separated branch
      4.3  Code modification
      4.4  Be sure that all tests of BinPY passes
      4.5  Commit the changes
      4.6  Writing commit messages
      4.7  Create a patch file or pull request for GitHub
      4.8  Updating your pull request
      4.9  Synchronization with master `BinPy/BinPy`.
        4.9.1  Merging
        4.9.2  Rebasing
        4.9.3  Changing of commit messages
    5  References

Introduction
============

BinPy encourages everyone to join and implement new features, fix some bugs, review pull requests and suggest ideas, take part in general discussions etc. 

General discussion takes place on `binpy@googlegroups.com`_ mailing list and
in the issues_. 

Discussions also take place on IRC (our channel is `#binpy-soc at freenode`_).

.. note::

   Our IRC channel is not logged, so when you don't get your answer from there, please post on the google group.

How to submit a patch
=====================

The best way to submit a patch is to send a GitHub pull request against the `BinPy <https://github.com/BinPy/BinPy>`_ repository. We'll review it and merge it with our code base.

Though patches can also be submitted as .patch file, it is highly recommended that you follow the GitHub Pull Request method.

The basic work-flow is as follows:

1. Create your environment, if it was not created earlier.
2. Create a new branch.
3. Modify code and/or create tests for it.
4. Be sure that all tests of BinPy pass. Make sure you repeat the tests with both python 2 and 3.
5. Only then commit changes. Follow commit message guidelines as given here.
6. After you commit make sure the code is properly indented using the `pep8` tool. If not use the `autopep8` tool to make the necessary formatting and recheck for `pep8` conformity. In rare cases you might need to manually make the changes.
7. Send the Pull Request on GitHub.

All those are described in the details below `Workflow process`_, but before
you read that, it would be useful to acquaint yourself with `Coding
conventions followed in BinPy`_.

.. hint::

   If you have any questions you can ask them on the `mailinglist`_.

Coding conventions in BinPy
===========================

Standard Python coding conventions
----------------------------------

We value clean code a lot and hence ` pep8 <http://www.python.org/dev/peps/pep-0008>`_ consistency check has been made mandatory. Please follow the standard Style Guide for Python Code when writing code for BinPy.

In particular,

- Use 4 spaces for indentation levels.

- Use all lowercase function names with words separated by
  underscores. For example, you are encouraged to write Python
  functions using the naming convention

  ::

      def print_output()

      def update_previous_bits()

  instead of the CamelCase convention.

- Use CamelCase for class names and major functions that create
  objects, e.g.

  ::

      class StateMachineSolver(object)

      class NBitRippleCounter()

.. note::

   Do not use tabs for indentation.

Note, however, that some functions do have uppercase letters where it makes sense. For example, `enabled_S`.

Documentation strings
---------------------

An example of a well formatted docstring::

        """
        This class is the primary medium for data transfer. Objects of this
        class can be connected to any digital object.

        Example
        =======

        >>> from BinPy import *
        >>> conn = Connector(1)  #Initializing connector with initial state = 1
        >>> conn.state
        1
        >>> gate = OR(0, 1)
        >>> conn.tap(gate, 'output')  #Tapping the connector

        Methods
        =======

        * tap
        * untap
        * isInputof
        * isOutputof
        * trigger

For more information see [[Writing documentation]] article on wiki.

Python 3
--------

BinPy uses a single codebase for Python 2 and Python 3 (the current supported
versions are Python 2.7, 3.2, 3.3 and 3.4). This means that your code needs
to run in both Python 2 and Python 3.

You may refer `this <http://stackoverflow.com/questions/8498823/how-to-write-python-2-x-as-much-compatible-with-python-3-x-as-possible>`_. as a ready reference to implement code that is both python 2 and 3 compatible.

You should also make sure that you have::

    from __future__ import print_function, division

at the top of each file. This will make sure that ``print`` is a function, and
that ``1/2`` does floating point division and not integer division. You should
also be aware that all imports are absolute, so ``import module`` will not
work if ``module`` is a module in the same directory as your file.  You will
need to use ``import .module``.

Workflow process
================

Create your environment
-----------------------

Creating of environment is once-only.

Install git
~~~~~~~~~~~

To install `git` in Linux-like systems you can do it via your native package management system: ::

    $ yum install git

or::

    $ sudo apt-get install git

In Windows systems, first of all, install Python from::

    http://python.org/download/

by downloading the "Python 2.7 Windows installer" and running it. Then do not
forget to add Python to the $PATH environment.

On Windows and Mac OS X, the easiest way to get git is to download GitHub's
software, which will install git, and also provide a nice GUI (this tutorial
will be based on the command line interface). Note, you may need to go into
the GitHub preferences and choose the "Install Command Line Tools" option to
get git installed into the terminal.

If you do decide to use the GitHub GUI, you should make sure that any "sync
does rebase" option is disabled in the settings.

Install other software
~~~~~~~~~~~~~~~~~~~~~~


Basic git settings
~~~~~~~~~~~~~~~~~~

Git tracks who makes each commit by checking the user’s name and email.
In addition, we use this info to associate your commits with your GitHub account.

To set these, enter the code below, replacing the name and email with your own (`--global` is optional).::

    $ git config --global user.name "Firstname Lastname"
    $ git config --global user.email "your_email@youremail.com"

The name should be your actual name, not your GitHub username.

These global options (i.e. applying to all repositories) are placed in `~/.gitconfig`.
You can edit this file to add setup colors and some handy shortcuts: ::

    [user]
        name = Firstname Lastname
        email = your_email@youremail.com

    [color]
        diff  = auto
        status= auto
        branch= auto
        interactive = true

    [alias]
        ci = commit
        di = diff --color-words
        st = status
        co = checkout
        log1 = log --pretty=oneline --abbrev-commit
        logs = log --stat

Advanced tuning
~~~~~~~~~~~~~~~
It can be convenient in future to tune the bash prompt to display the current git branch.

The easiest way to do it, is to add the snippet below to your .bashrc or .bash_profile::

    PS1="[\u@\h \W\$(git branch 2> /dev/null | grep -e '\* ' | sed 's/^..\(.*\)/{\1}/')]\$ "

But better is to use `git-completion` from the `git` source. This also has the advantage of adding tab completion to just about every git command. It also includes many other useful features, for example,
promptings. To use `git-completion`, first download the `git` source code (about 27 MiB), then copy
the file to your profile directory::

    $ git clone git://git.kernel.org/pub/scm/git/git.git
    $ cp git/contrib/completion/git-completion.bash ~/.git-completion.sh

Read instructions in '~/.git-completion.sh'

Note that if you install git from the package manager in many Linux distros, this file is already installed for you.  You can check if it is installed by seeing if tab completion works on git commands (try, e.g., `git commi<TAB>`, or `git log --st<TAB>`). You can also check if the PS1 commands work by doing something like::

    $ PS1='\W $(__git_ps1 "%s")\$ '

And your command prompt should change to something like::

    BinPy master$

.. note::

   It is important to define your PS1 using single quotes ('), not double quotes ("), or else bash will not update the branch name.


Create GitHub account
~~~~~~~~~~~~~~~~~~~~~

As you are going to use `GitHub`_  you should have a GitHub account. If you have not one yet then sign up at:

    - https://github.com/signup/free

Then create your own *fork* of the BinPy project (if you have not yet). Go to the BinPy GitHub repository:

    - https://github.com/BinPy/BinPy

and click the “Fork” button.

Now you have your own repository for the BinPy project. If your username in GitHub is `mynick` then the address of the forked project will look something like:

    - https://github.com/mynick/BinPy


Cloning BinPy
~~~~~~~~~~~~~

On your machine browse to where you would like to clone BinPy, and clone (download) the latest
code from BinPy's original repository::

    $ git clone git://github.com/BinPy/BinPy.git
    $ cd BinPy

Then assign your read-and-write repo to a remote called "github"::

    $ git remote add github git@github.com:mynick/BinPy.git


Create separated branch
-----------------------

Typically, you will create a new branch to begin work on a new issue. Also pull request related with them.

A branch name should briefly describe the topic of the patch or pull request.
If you know the issue number, then the branch name could be, for example, `1234_sequences`. To create
and checkout (that is, make it the working branch) a new branch ::

    $ git branch 123_sequential
    $ git checkout 123_sequential

or in one command using ::

    $ git checkout -b 123_sequential

To view all branches, with your current branch highlighted, type::

    $ git branch

And remember, **never type the following commands in master**: `git merge`, `git commit`, `git rebase`.

Code modification
-----------------

Do not forget that all new functionality should be tested, and all new methods, functions, and classes should have doctests showing how to use them.


Be sure that all tests of BinPy_ pass
-------------------------------------

To see if all tests pass::

    $ cd BinPy/BinPy/tests
    $ nosetests && nosetests3

Remember that all tests should pass before committing.

Note that all tests will be run when you make your pull request automatically
by Travis CI.

Commit the changes
------------------

You can check what files are changed::

    $ git status

Add new files to the index if necessary::

    $ git add new_file.py

Check total changes::

    $ git diff

You are ready to commit changes locally. A commit also contains a `commit
message` which describes it.  See the next section for guidelines on writing
good commit messages. Type::

    $ git commit

An editor window will appear automatically in this case. In Linux, this is vim by default. You
can change what editor pops up by changing the `$EDITOR` shell variable.

Also with the help of option `-a` you can tell the command `commit` to automatically stage files
that have been modified and deleted, but new files you have not told git about will not be
affected, e.g.,::

    $ git commit -a

If you want to stage only part of your changes, you can use the interactive commit feature.  Just type::

    $ git commit --interactive

and choose the changes you want in the resulting interface.


Writing commit messages
-----------------------

There are only two formatting rules for commit messages

- All lines should be 78 characters or less.  This is so they can be easily
  read in terminals, which don't automatically line wrap things.

- There should be a single line with a summary, then an empty line, followed
  by (optional) additional details.  A common convention is to not end the
  first line with a ``.``, but all additional lines should (this convention
  probably exists to save an extra character to make it easier to fit the
  first line summary in 78 characters).

Some things to note about An ideal commit message:

- The first line gives a brief description of what the commit does. Tools like
  ``git shortlog`` or even GitHub only show the first line of the commit by
  default, so it is important to convey the most important aspects of the
  commit in the first line.

- The first line starts with a key word which gives context to the commit. A
  commit won't always be seen in the context of your branch, so it is often
  helpful to give each commit some context. This is not required, though, as
  it is not hard to look at the commit metadata to see what files were
  modified or at the commit history to see the nearby related commits.

- After the first line, there is a paragraph describing the commit in more
  detail. This is important, as it describes what the commit does, which might
  be hard to figure out just from looking at the diff. It also gives
  information that might not be in the diff at all, such as known issues. Such
  paragraphs should be written in plain English. Commit messages are intended
  for human readers, both for people who will be reviewing your code right
  now, and for people who might come across your commit in the future while
  researching some change in the code. Sometimes, bulleted lists are a good
  format to convey the changes of a commit.

- Last, there is an example.  It is nice to give a concrete example in commits
  that add new features.  This particular example is about improving the speed
  of something, so the example is a benchmark result.

**Other things to do in commit messages:**

- **If the bug fixes an issue, reference that issue in the message (with a string like
  ``closes #123``, see `this <https://help.github.com/articles/closing-issues-via-commit-messages>`_
  for exact syntax reference)**. Also
  reference any pull requests or mailing list messages with links. This will
  make it easier to find related discussions about the commit in the
  future. You do not need to add a reference to the pull request that contains
  the commit. That can be found from the git log.

Try to avoid short commit messages, like "Fix", and commit messages that give
no context, like "Found the bug".  When in doubt, a longer commit message is
probably better than a short one.

Create a patch file or pull request for GitHub
----------------------------------------------

Be sure that you are in your own branch, and run::

    $ git push github 123_sequential

This will send your local changes to *your* fork of the BinPy repository.
Then navigate to your repository with the changes you want someone else to pull:

    https://github.com/mynick/BinPy

Select branch, and press the `Pull Request` button.


After pressing the `Pull Request` button, you are presented with a preview page where you can
enter a title and optional description, see exactly what commits will be included when the pull
request is sent, and also see who the pull request will be sent to

If you’re sending from a topic branch, the title is pre-filled based on the name of the branch.
Markdown is supported in the description, so you can embed images or use preformatted text blocks.

You can switch to the `Commits` tab to ensure that the correct set of changes is being sent.
And review the diff of all changes by switching to the `Files Changed`.

Once you’ve entered the title and description, made any necessary customizations to the commit
range, and reviewed the commits and file changes to be sent, press the `Send pull request` button.

The pull request is sent immediately. You’re taken to the main pull request discussion and review
page. Additionally, all repository collaborators and followers will see an event in their dashboard.

That's all.

See also `Updating your pull request`_


Updating your pull request
--------------------------

If after a time you need to make changes in pull request then the best way is to add a new commit
in you local repository and simply repeat push command::

    $ git commit
    $ git push github 123_sequential

Note that if you do any rebasing or in any way edit your commit history, you will have to add
the `-f` (force) option to the push command for it to work::

    $ git push -f github

You don't need to do this if you merge, which is the recommended way.

Synchronization with master `BinPy/BinPy`.
------------------------------------------

Sometimes, you may need to merge your branch with the upstream master. Usually
you don't need to do this, but you may need to if

- Someone tells you that your branch needs to be merged because there are
  merge conflicts.

- While raising a Pull Request, you get a message from github telling you that your branch could not be merged.

- You need some change from master that was made after you started your branch.

Note, that after cloning a repository, it has a default remote called `origin`
that points to the `BinPy/BinPy` repository.  And your fork remote named as
`github`. You can observe the remotes names with the help of this command::

    $ git remote -v
    github  git@github.com:mynick/BinPy.git (fetch)
    github  git@github.com:mynick/BinPy.git (push)
    origin  git://github.com/BinPy/BinPy.git (fetch)
    origin  git://github.com/BinPy/BinPy.git (push)


As an example, consider that we have these commits in the master branch of local git repository::

    A---B---C        master

Then we have divergent branch `123_sequential`::


    A---B---C           master
             \
              a---b     123_sequential

In the meantime the remote `BinPy/BinPy` master repository was updated too::

    A---B---C---D       origin/master
    A---B---C           master
             \
              a---b     123_sequential

There are basically two ways to get up to date with a changed master: rebasing
and merging.  Merging is recommended.

Merging creates a special commit, called a "merge commit", that joins your
branch and master together::

    A---B---C------D       origin/master
             \      \
              \      M     merge
               \    /
                a--b       123_sequential


Note that the commits ``A``, ``B``, ``C``, and ``D`` from master and the
commits ``a`` and ``b`` from ``123_sequential`` remain unchanged. Only the new
commit, ``M``, is added to ``123_sequential``, which merges in the new commit
branch from master.

Rebasing essentially takes the commits from ``123_sequential`` and reapplies
them on the latest master, so that it is as if you had made them from the
latest version of that branch instead.  Since these commits have a different
history, they are different (they will have different SHA1 hashes, and will
often have different content)::

    A---B---C---D---a'---b' origin/master

Rebasing is required if you want to edit your commit history (e.g., squash
commits, edit commit messages, remove unnecessary commits). But note that
since this rewrites history, it is possible to lose data this way, and it
makes it harder for people reviewing your code, because they can no longer
just look at the "new commits"; they have to look at everything again, because
all the commits are effectively new.

There are several advantages to merging instead of rebasing.  Rebasing
reapplies each commit iteratively over master, and if the state of the files
changed by that commit is different from when it was originally made, the
commit will change.  This means what you can end up getting commits that are
broken, or commits that do not do what they say they do (because the changes
have been "rebased out").  This can lead to confusion if someone in the future
tries to test something by checking out commits from the history.  Finally,
merge conflict resolutions can be more difficult with rebasing, because you
have to resolve the conflicts for each individual commit.  With merging, you
only have to resolve the conflicts between the branches, not the commits.  It
is quite common for a merge to not have any conflicts but for a rebase to have
several, because the conflicts are "already resolved" by later commits.

Merging keeps everything intact.  The commits you make are exactly the same,
down to the SHA1 hash, which means that if you checkout a commit from a merged
branch, it is exactly the same as checking it out from a non-merged branch.
What it does instead is create a single commit, the merge commit, that makes
it so that the history is both master and your branch.  This commit contains
all merge conflict resolution information, which is another advantage over
rebasing (all merge conflict resolutions when rebasing are "sifted" into the
commits that caused them, making them invisible).

Since this guide is aimed at new git users, you should be learning how to
merge.

Merging
~~~~~~~

First merge your local repository with the remote::

    $ git checkout master
    $ git pull

This results in::

    A---B---C---D       master
             \
              a---b     123_sequential

Then merge your `123_sequential` branch from `123_sequential`::

    $ git checkout 123_sequential
    $ git merge master

If the last command tells you that conflicts must be solved for a few indicated files.

If that's the case then the marks **>>>** and **<<<** will appear at those files. Fix the
code with **>>>** and **<<<** around it to what it should be.
You must manually remove useless pieces, and leave only new changes from your branch.

Then be sure that all tests pass::

    $ cd BinPy/BinPy/tests
    $ nosetests && nosetests3

and commit::

    $ git commit

So the result will be like that (automatic merging `c`)::

    A---B---C-------D     master
             \       \
              a---b---M   123_sequential



Rebasing
~~~~~~~~

***Note*: merging is recommended over rebasing.**

The final aim, that we want to obtain is::

    A---B---C---D           master
                 \
                  a---b     123_sequential

The way to do it is first of all to merge local repository with the remote `BinPy/BinPy`::

    $ git checkout master
    $ git pull

So we obtain::

    A---B---C---D       master
             \
              a---b     123_sequential

Then::

    $ git checkout 123_sequential
    $ git rebase master

Note that this last one will require you to fix some merge conflicts if there are changes
to the same file in ``master`` and ``123_sequential``. Open the file that it tells you is wrong,
fix the code with **>>>** and **<<<** around it to what it should be.

Then be sure that all tests pass::

    $ cd BinPy/BinPy/tests
    $ nosetests && nosetests3

Then do::

    $ git add BinPy/BinPy/Sequential/your_conflict_file
    $ git rebase --continue

(git rebase will also guide you in this).

Changing of commit messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only time when it is recommended to rebase instead of merge is when you
need to edit your commit messages, or remove unnecessary commits.

Note, it is much better to get your commit messages right the first time.  See
the section on writing good commit messages above.

Consider these commit messages::

    $ git log --oneline
    7bbbc06 bugs fixing
    4d6137b some additional corrections.
    925d88fx sequences base implementation.


Then run *rebase* command in interactive mode::

    $ git rebase --interactive 925d88fx

Or you can use other ways to point to commits, e.g. *`git rebase --interactive HEAD^^`*
or *`git rebase --interactive HEAD~2`*.

A new editor window will appear (note that order is reversed with respect to the `git log` command)::

    pick 4d6137b some additional corrections.
    pick 7bbbc06 bugs fixing

    # Rebase 925d88f..7bbbc06 onto 925d88f
    #
    # Commands:
    #  p, pick = use commit
    #  r, reword = use commit, but edit the commit message
    #  e, edit = use commit, but stop for amending
    #  s, squash = use commit, but meld into previous commit
    #  f, fixup = like "squash", but discard this commit's log message

To edit a commit message, change *pick* to *reword* (or on old versions of
git, to *edit*) for those that you want to edit and save that file.

To squash two commits together, change *pick* to *squash*. To remove a commit,
just delete the line with the commit.

To edit a commit, change *pick* to *edit*.

After that, git will drop you back into your editor for every commit you want to reword,
and into the shell for every commit you wanted to edit::

    $ (Change the commit in any way you like.)
    $ git commit --amend -m "your new message"
    $ git rebase --continue

For commits that you want to edit, it will stop. You can then do::

    $ git reset --mixed HEAD^

This will "uncommit" all the changes from the commit. You can then recommit
them however you want. When you are done, remember to do::

    $ git rebase --continue

Most of this sequence will be explained to you by the output of the various commands of git.
Continue until it says: ::

    Successfully rebased and updated refs/heads/master.

If at any point you want to abort the rebase, do::

   $ git rebase --abort

.. warning::

   This will run ``git reset --hard``, deleting any uncommitted
   changes you have. If you want to save your uncommitted changes, run ``git
   stash`` first, and then run ``git stash pop`` when you are done.

Reviewing patches
=================
Coding's only half the battle in software development: our code also has to be
thoroughly reviewed before release. Reviewers thus are an integral part of the
development process. Note that you do *not* have to have any special pull
or other privileges to review patches: anyone with Python on his/her computer
can review.

Pull requests (the preferred avenue for patches) for BinPy are located
`here <https://github.com/BinPy/BinPy/pulls>`_. Feel free to view any open
pull request. Each contains a Discussion section for comments, Commits section
for viewing the author's commit files and documentation, and Diff section for
viewing all the changes in code. To browse the raw code files for a commit, select
a commit in the Commits section and click on the "View file" link to view a file.

Based on your level of expertise, there are two ways to participate in the
review process: manually running tests. Whichever option
you choose, you should also make sure that the committed code complies with
the [[Writing documentation]] guidelines.

Manual testing
--------------
If you prefer to test code manually, you will first have to set up your
environment as described in the Workflow process section. Then, you need to
obtain the patched files. If you're reviewing a pull request, you should get
the requested branch into your BinPy folder. Go into your folder and execute
(<username> being the username of the pull requester and <branchname> being
the git branch of the pull request)::

    $ git remote add <username> git://github.com/<username>/BinPy.git
    $ git fetch <username>
    $ git checkout -b <branchname> <username>/<branchname>

After obtaining the pull request or patch, go to your BinPy root directory and
execute::

    $ cd BinPy/BinPy/tests
    $ nosetests && nosetests3

If there are any problems, notify the author in the pull request by commenting.


Requirements for inclusion
--------------------------
A pull request or patch must meet the following requirements during review
before being considered as ready for release.

- All tests must pass.
    - Rationale: We need to make sure we're not releasing buggy code.
    - If new features are being implemented and/or bug fixes are added,
      tests should be added for them as well.
- The reviews (at least 1) must all be positive.
    - Rationale: We'd like everyone to agree on the merits of the patch.
    - If there are conflicting opinions, the reviewers should reach a consensus.
- The patch must have been posted for at least 24 hours.
    - Rationale: This gives a chance for everyone to look at the patch.


References
==========
.. .. rubric:: Footnotes

.. [1] http://lkml.org/lkml/2000/8/25/132
.. [2] https://github.com/BinPy/BinPy/wiki
.. [3] https://github.com/BinPy/BinPy/wiki/Pushing-patches
.. [4] https://github.com/BinPy/BinPy/wiki/Download-Installation
.. [5] http://help.github.com/pull-requests/
.. [6] http://help.github.com/fork-a-repo/
.. [7] http://sagemath.org/doc/developer/
.. [8] http://help.github.com/linux-set-up-git/




.. _BinPy:          http://BinPy.org/
.. _issues:         http://www.github.com/BinPy/BinPy/issues
.. _mailinglist:    BinPy@googlegroups.com_
.. _BinPy@googlegroups.com:             http://groups.google.com/group/BinPy
.. _LICENSE:            https://github.com/BinPy/BinPy/blob/master/LICENSE
.. _GitHub:             https://github.com/
.. _BinPy/BinPy:        https://github.com/BinPy/BinPy
.. _`#BinPy at freenode`:                 irc://irc.freenode.net/BinPy