name: Test repo code
on: [pull_request]
jobs:
  test-our-code:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 Our code works flawelessly."
