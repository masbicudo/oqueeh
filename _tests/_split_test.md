#file=_test/_output/depC1.md
    #include=_test/_output/cyc1.md

#file=_test/_output/cyc1.md
    Cycle 1
    #include=_test/_output/cyc2.md

#file=_test/_output/cyc2.md
    Cycle 2
    #include=_test/_output/cyc1.md

#file=_test/_output/cycS.md
    Cycle self
    #include=_test/_output/cycS.md

#file=_test/_output/depCS.md
    #include=_test/_output/cycS.md

#file=_test/_output/dupe.md
    Dupe 1

#file=_test/_output/dupe.md
    Dupe 2

#file=_test/_output/no-ext
    No extension

#file=_test/_output/dep3.md
    Dependency 3
    #ref=some.md

#file=_test/_output/dep1.md
    #include=dep3.md
    #include=dep2.md
    Dependency 1

#file=_test/_output/some.md
    #include=dep1.md
    Something here!

#file=_test/_output/dep2.md
    Dependency 2

#file=_test/_output/not-error.md
    xpto #overwrite=1
    Not-error: text before directive
    The line is not interpreted as having a directive at all

#file=
    Empty file name

#file=_test/_output/
    Empty file name

#file=_test/_output/x.xpto
    Invalid extension

#file=_test/_output/errdir.md
    #strange=123

#file=_test/_output/err-multititle.md
    # Multi-title
    # Other title
