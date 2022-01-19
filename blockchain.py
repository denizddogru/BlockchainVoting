# -*- coding: utf-8 -*-

import hashlib
from datetime import datetime, date

class Block:
  def __init__(self, data, previousHash=''):
    self.data = data   # list of 3 items such as [1,5,50]
    self.timestamp = datetime.now()
    self.previousHash = previousHash
    self.hash = self.addHash()
  def addHash(self):
    block_hash = hashlib.sha256()
    data = '-'.join(map(str, self.data))
    block_hash.update((data+self.timestamp.isoformat()+self.previousHash).encode('utf-8'))
    return block_hash.hexdigest()

class BlockChain:
  def __init__(self):    
    self.chain = [self.genesisBlock()]
  def genesisBlock(self):
    return Block([],'000')
  def lastChain(self):
    return self.chain[-1]
  def addBlock(self,newblock):
    newblock.previousHash = self.lastChain().hash
    newblock.hash = newblock.addHash()
    self.chain.append(newblock)
    
    with open("blockchain.txt", "r") as file1:
      first_line = file1.readline()
    if first_line == "":
      file2=open("blockchain.txt", "a")      
      file2.write("Block 0 Hash: "+str(self.chain[0].hash)+"\n")
      file2.write("Previous Block Hash: 000\n")
      file2.write("\n")
      file2.write("Block "+str(len(self.chain)-1)+" Hash: "+str(newblock.hash)+"\n")
      file2.write("Previous Block Hash: "+str(self.chain[0].hash)+"\n")
      file2.close()

    elif "Block 0 Hash" in first_line:
      file3=open("blockchain.txt", "r")
      linelist = file3.readlines()
      previous_hash_str = linelist[len(linelist)-2]
      current_line = previous_hash_str.split(":")
      previous_hash = current_line[1].strip()
      temp_list = current_line[0].strip().split(" ")
      line_number = int(temp_list[1])
      file3.close()
      file4=open("blockchain.txt", "a")
      file4.write("\n")
      file4.write("Block "+str(line_number+1)+" Hash: "+str(newblock.hash)+"\n")
      file4.write("Previous Block Hash: "+str(previous_hash)+"\n")
      file4.close()

  def chainValid(self):
    for index in range(1,len(self.chain)):
      block = self.chain[index]
      previous_block = self.chain[index-1]
    if (block.hash != block.addHash()):
      return False
    elif (block.previousHash != previous_block.hash):
      return False
    else:
      return True



# Blockchain başlatılıyor
Ycoin = BlockChain()


def add_block(blockdata):
  # GUI'den gelen kayıtlar blockchain'e yazılıyor
  # username-password-vote
  Ycoin.addBlock(Block(blockdata))
  

def Valid_check():
  # blockchain valid mi diye kontrol ediliyor
  print("Is Blockhain Valid:",Ycoin.chainValid(),"\n")

def print_blockchain():
  # Blocktaki data, block'un hashi ve önceki block'un hash'i ekrana basılıyor
  i = 0
  for block in Ycoin.chain:
    print("Blok",i,"Data :",block.data)
    print("Block",i, "Hash:",block.hash)
    print("Previous Block Hash:",block.previousHash)
    print("\n")
    i+=1

