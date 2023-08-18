import os
class GenHTML():

    def __init__(self,sticker, num_inicial, num_final=''):
        self.num_inicial = num_inicial
        self.num_final = num_final
        self.sticker = sticker
        if self.num_final == '':
            self.tipo = 'unitario'
        else:
            self.tipo = 'lista'
        self.lista_codigos = []

        if self.sticker == 'estandar':
            self.html_original = '<head><link rel="stylesheet" href="estilo.css"></head><body><div class="sticker-container"><table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr> <tr><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td></tr><tr><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><td>29</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>35</td></tr><tr><td>36</td><td>37</td><td>38</td><td>39</td><td>40</td><td>41</td><td>42</td></tr></table></div></body>'
        elif self.sticker == 'mini':
            self.html_original = '<head><link rel="stylesheet" href="./sources/estilo.css"/></head><body><div class="sticker-container"><table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><td>29</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>35</td><td>36</td><td>37</td><td>38</td><td>39</td><td>40</td><td>41</td><td>42</td></tr><tr><td>43</td><td>44</td><td>45</td><td>46</td><td>47</td><td>48</td><td>49</td><td>50</td><td>51</td><td>52</td><td>53</td><td>54</td><td>55</td><td>56</td></tr><tr><td>57</td><td>58</td><td>59</td><td>60</td><td>61</td><td>62</td><td>63</td><td>64</td><td>65</td><td>66</td><td>67</td><td>68</td><td>69</td><td>70</td></tr><tr><td>71</td><td>72</td><td>73</td><td>74</td><td>75</td><td>76</td><td>77</td><td>78</td><td>79</td><td>80</td><td>81</td><td>82</td><td>83</td><td>84</td></tr><tr><td>85</td><td>86</td><td>87</td><td>88</td><td>89</td><td>90</td><td>91</td><td>92</td><td>93</td><td>94</td><td>95</td><td>96</td><td>97</td><td>98</td></tr><tr><td>99</td><td>100</td><td>101</td><td>102</td><td>103</td><td>104</td><td>105</td><td>106</td><td>107</td><td>108</td><td>109</td><td>110</td><td>111</td><td>112</td></tr><tr><td>113</td><td>114</td><td>115</td><td>116</td><td>117</td><td>118</td><td>119</td><td>120</td><td>121</td><td>122</td><td>123</td><td>124</td><td>125</td><td>126</td></tr><tr><td>127</td><td>128</td><td>129</td><td>130</td><td>131</td><td>132</td><td>133</td><td>134</td><td>135</td><td>136</td><td>137</td><td>138</td><td>139</td><td>140</td></tr><tr><td>141</td><td>142</td><td>143</td><td>144</td><td>145</td><td>146</td><td>147</td><td>148</td><td>149</td><td>150</td><td>151</td><td>152</td><td>153</td><td>154</td></tr><tr><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>167</td><td>168</td></tr><tr><td>169</td><td>170</td><td>171</td><td>172</td><td>173</td><td>174</td><td>175</td><td>176</td><td>177</td><td>178</td><td>179</td><td>180</td><td>181</td><td>182</td></tr><tr><td>183</td><td>184</td><td>185</td><td>186</td><td>187</td><td>188</td><td>189</td><td>190</td><td>191</td><td>192</td><td>193</td><td>194</td><td>195</td><td>196</td></tr><tr><td>197</td><td>198</td><td>199</td><td>200</td><td>201</td><td>202</td><td>203</td><td>204</td><td>205</td><td>206</td><td>207</td><td>208</td><td>209</td><td>210</td></tr><tr><td>211</td><td>212</td><td>213</td><td>214</td><td>215</td><td>216</td><td>217</td><td>218</td><td>219</td><td>220</td><td>221</td><td>222</td><td>223</td><td>224</td></tr><tr><td>225</td><td>226</td><td>227</td><td>228</td><td>229</td><td>230</td><td>231</td><td>232</td><td>233</td><td>234</td><td>235</td><td>236</td><td>237</td><td>238</td></tr><tr><td>239</td><td>240</td><td>241</td><td>242</td><td>243</td><td>244</td><td>245</td><td>246</td><td>247</td><td>248</td><td>249</td><td>250</td><td>251</td><td>252</td></tr></table></div></body>'

    def generarLista(self):
        if self.tipo == 'lista' :
            for x in range(self.num_inicial, self.num_final+1):
                self.lista_codigos.append(x)
            return self.lista_codigos
        else:
            self.lista_codigos.append(self.num_inicial)
            return self.lista_codigos

    def generarDiv(self, codigo):
        reemplazar = codigo
        if self.sticker == 'estandar':
            div = f'<td class="{self.sticker}"><div class="sticker"><div class="titulo">INVENTARIO ACTIVO FIJO 2023</div><div class="qr"><img src="file:///D:/Scripts/modulo_qr/sources/{reemplazar}.png" alt=""/></div><div class="codigo"><p>{reemplazar}</p></div><div class="colegio"><div class="logo"></div><div class="nombre"><p>San José Maristas</p></div></div><div class="pie"><p>SIGMA MTI</p></div></div></td>'
        elif self.sticker == 'mini':
            div = f'<td class="{self.sticker}"><div class="mini-sticker"><div class="mini-qr"><img src="file:///D:/Scripts/modulo_qr/sources/{reemplazar}.png" alt=""></div><div class="mini-codigo"><p>{reemplazar}</p></div></div></td>'
        return div

    def editarTD(self, numero_td, codigos_a_generar):
        td = numero_td
        codigo = codigos_a_generar
        valores = [f"<td>{td}</td>",f"{self.generarDiv(codigo)}"]
        self.html_original = self.html_original.replace(valores[0],valores[1])
        return f'{self.html_original}'

    def eliminar(self):
        pass

    def crear(self):
        contador_ediciones = 0
        datos = self.generarLista()
        for dato in datos:
            contador_ediciones += 1
            self.editarTD(contador_ediciones, dato)
        #Generar el archivo
        hoja_html = open("./sources/temporal.html", "w",encoding='utf-8')
        hoja_html.write(f'{self.html_original}')
        hoja_html.close()


    def __str__(self):
        contador_ediciones = 0
        datos = self.generarLista()
        for dato in datos:
            contador_ediciones += 1
            self.editarTD(contador_ediciones, dato)
        #Generar el archivo
        hoja_html = open("./sources/temporal.html", "w",encoding='utf-8')
        hoja_html.write(f'{self.html_original}')
        hoja_html.close()
        #Reporte de lo generado en consola
        return f'{self.html_original}'

if __name__ == '__main__':
    lista1 = GenHTML(10,12)
    print(lista1)
