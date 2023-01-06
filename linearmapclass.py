import matrices as mp

class LinearMapping:
  def __init__(self, A, B, mapping=None):
    self.matrix = A
    self.matrix1 = B
    self.domain = [row[:] for row in A]
    self.codomain = [row[:] for row in B]
    self.mapping = mapping # needs to be a matrix or None
    self.injective = True if mp.rank(self.mapping) == len(self.mapping[0]) else False
    self.surjective = True if mp.rank(self.mapping) == len(self.mapping) else False
    self.bijective = True if (self.injective == True and self.surjective == True) else False
    self.homomorphism = True # (by definition, duh)
    self.isomorphism = True if (self.bijective == True) else False # homomorphism already satisfied
    self.is_endomorphism  = None # True if dim(A) == dim(B) and len(A[0]) == len(B[0]) else False
    self.is_  

  def map(self, vector):
        return self.apply(vector)

  def apply_mapping(self, vector):

    # expects a vector in the domain, not codomain
    # will then apply the linear mapping (self.mapping) to the vector
    # will return the result
    return mp.multiply_matrix(self.mapping, mp.transpose([vector]))

    # OLD ################## OLD
    # Check that the input vector is in the correct domain
    # if len(vector) != len(self.domain[0]):
    #   raise ValueError("Vector has incorrect dimension for the specified domain")

    # # Apply the linear mapping to the input vector
    # result = [0 for _ in range(len(self.codomain[0]))]
    # for i in range(len(self.matrix)):
    #   for j in range(len(vector)):
    #     result[i] += self.matrix[i][j] * vector[j]
    # return result

  def is_subspace(self, subspace):
      # check if subspace is a part of vector_space_1
      for vector in subspace:
          if vector not in self.matrix:
              return False
      return True

  def is_homomorphism(self):
      # check if the mapping preserve vector addition
      for vector_1 in self.matrix:
          for vector_2 in self.matrix1:
              mapped_vector_1 = self.map(vector_1)
              mapped_vector_2 = self.map(vector_2)
              if mapped_vector_1 + mapped_vector_2 != self.map(vector_1 + vector_2):
                  return False
      return True

  def is_isomorphism(self):
      # check if the mapping is bijective and preserve vector addition
      if not self.is_homomorphism():
          return False

        # check if the mapping is surjective
      for vector in self.matrix1:
          if vector not in self.map(self.matrix):
              return False

        # check if the mapping is injective
      for i, vector_1 in enumerate(self.matrix):
          for j, vector_2 in enumerate(self.matrix):
              if i != j and self.map(vector_1) == self.map(vector_2):
                  return False

      return True

  def is_endomorphism(self):
      # check if the mapping is from a vector space to itself and preserve vector addition
      return self.matrix == self.matrix1 and self.is_homomorphism()

# Test the LinearMapping class
A = [[1, 2], [3, 4]]
B = [[5, 6, 7], [8, 9, 10],[11, 12, 13]]
C = [[1,3],[2,3],[2,4]]
lm = LinearMapping(A, B, mapping=C)
# subspac1e = [1,2]
# result = lm.apply_mapping(subspac1e)
# print(result)  