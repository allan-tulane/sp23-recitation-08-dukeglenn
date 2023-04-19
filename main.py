
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
  m, n = len(S), len(T)
  dp = [[0] * (n + 1) for _ in range(m + 1)]
  for i in range(1, m + 1):
    dp[i][0] = i
  for j in range(1, n + 1):
    dp[0][j] = j
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if S[i - 1] == T[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
  return dp[m][n]


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
  elif (S == ""):
    return(len(T))
  elif (T == ""):
    return(len(S))
  else:
    if (S[0] == T[0]):
      MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
      MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))
  return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
  
  
  if (S, T) in MED:
    return MED[(S, T)]
  elif (T, S) in MED:
      return MED[(T, S)]

  if (S == ""):
    return(len(T))
  elif (T == ""):
    return(len(S))
  else:
    if (S[0] == T[0]):
      FAM = fast_align_MED(S[1:], T[1:], MED)
      return(S[0] + FAM, T[0] + FAM)
    else:
      case_1 = fast_MED(S, T[1:], MED)
      case_2 = fast_MED(S[1:], T, MED)
      case_3 = fast_MED(S[1:], T[1:], MED) 

      case_1FAM = fast_align_MED(S, T[1:], MED)
      case_2FAM = fast_align_MED(S[1:], T, MED)
      case_3FAM = fast_align_MED(S[1:], T[1:], MED)  
      
      FM = min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))

      if FM == case_1:
        FAM = case_1FAM
        return('-' + FAM, T[0] + FAM)
      elif FM == case_2:
        FAM = case_2FAM
        return(S[0] + FAM, '-' + FAM)
      elif FM == case_3:
        FAM = case_3FAM
        return(S[0] + FAM, T[0] + FAM)
  
  return FM
  pass



def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])