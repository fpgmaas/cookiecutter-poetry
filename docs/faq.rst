==========================
Frequently Asked Questions
===========================

Note: If you get an error in the shape of 
```
error: src refspec main does not match any
error: failed to push some refs to 'github.com:fpgmaas/example-project.git'
```

you are likely still using ``master`` as the default branch. You can change this with:


`git config --global init.defaultBranch main`