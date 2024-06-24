module Jekyll
  module HashAssignFilter
    def hash_assign(hash, key, value)
      hash[key] = value
      hash
    end
  end
end

Liquid::Template.register_filter(Jekyll::HashAssignFilter)