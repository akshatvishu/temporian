package(
    default_visibility = ["//visibility:public"],
    licenses = ["notice"],
)

# Tests
# =====

py_test(
    name = "evaluation_test",
    srcs = ["evaluation_test.py"],
    srcs_version = "PY3",
    deps = [
        # already_there/absl/testing:absltest
        # already_there/absl/testing:parameterized
        # already_there/google/protobuf:use_fast_cpp_protos
        "//temporian/implementation/numpy/data:io",
        "//temporian/beam/test:utils",
        "//temporian/core/operators:select",
        "//temporian/core/operators/window:moving_sum",
    ],
)

# Libraries
# =========

py_library(
    name = "utils",
    srcs = ["utils.py"],
    srcs_version = "PY3",
    deps = [
        "//temporian/core/data:dtype",
        # already_there/absl/testing:absltest
        # already_there/absl/testing:parameterized
        # already_there/apache_beam
        "//temporian/test:utils",
        "//temporian/beam/io:csv",
        "//temporian/beam/io:tensorflow",
        "//temporian/beam:evaluation",
        "//temporian/io:csv",
        "//temporian/io:tensorflow",
        "//temporian/core/data:node",
        "//temporian/implementation/numpy/data:event_set",
    ],
)
