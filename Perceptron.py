class Percetron:
      w =[] ;
      matrix = [];
      def __init__(self):
           self.w = [0,0];
           self.interacao  =10000;
           self.output = [0,1,1,0];
           self.bias =0;
           self.matrix :[] = [
                [0,0]
               ,[0,1]
               ,[1,0]
               ,[1,1]
           ];

      def  FuncaoActivacao(self ,x1, x2):
           soma = (x1 *self.w[0] +  x2 * self.w[1]) - self.bias;
           if  soma >=0 :
               return 1;
           else:
               return  0;

      def  Treinar(self):
           for i in range(self.interacao):
              for  index  in range(len(self.matrix)):
                 saida = self.FuncaoActivacao(self.matrix[index][0] ,self.matrix[index][1]);
                 #currgindo os  pesos para melhor ajustes
                 self.w[0] = self.w[0] +  (self.output[index] -  saida) * (self.matrix[index][0]);
                 self.w[1] = self.w[1] +  (self.output[index] -  saida) * (self.matrix[index][1]);
                 self.bias = self.bias -  (self.output[index] -  saida);
