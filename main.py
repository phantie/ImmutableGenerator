class ImmutableGenerator:
    def __init__(self, generator_factory):
        self.generator_factory = generator_factory

        self.no_result = object()
        self.cached_result = self.no_result

    def __iter__(self):
        return self

    def __next__(self):
        if self.cached_result is not self.no_result:
            return self.cached_result

        g = self.generator_factory()
        next_value = next(g)

        self.cached_result = ( 
            next_value,
            self.__class__(lambda: g))

        return self.cached_result
