# Bazel Build

## Resources
- Official site: https://www.bazel.build/
- Examples:
```
git clone https://github.com/bazelbuild/examples
```

## Bazel for cpp
- https://docs.bazel.build/versions/master/tutorial/cpp.html
- Build:
```
bazel build //main:hello-world
```
- Run:
```
bazel-bin/main/hello-world
```
- Visualize dependency (paste and visualizable in http://www.webgraphviz.com/):
```
bazel query --notool_deps --noimplicit_deps 'deps(//main:hello-world)'   --output graph
```