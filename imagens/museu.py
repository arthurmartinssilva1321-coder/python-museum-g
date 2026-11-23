import os
import tkinter as tk
from PIL import Image, ImageTk

PASTA = os.path.dirname(os.path.abspath(__file__))

fases = [
    {"nome": "Pré-Cambriano", "itens": [
        {"img": "KRW-Magma_Dopant.webp", "texto": "O mascote da sala do Pré-Cambriano, Senhor Magzor, representa a fase da formação da Terra, ocorrida há 4,5 bilhões de anos, chamada de Hadeano."},
        {"img": "dick.png", "texto": "Misterioso organismo do final do Pré-Cambriano, considerado um dos primeiros animais da Terra."},
        {"img": "estromatólito.png", "texto": "Estrutura rochosa laminada formada pela atividade de colônias de microrganismos fotossintetizantes, principalmente cianobactérias."},
        {"img": "ediacara.jpg", "texto": "Imagem do ecosistema do período Ediacarano, caracterizado por organismos de formas incomuns e complexas."},
    ]},
    {"nome": "Paleozoico", "itens": [
        {"img": "masotedopaleozoico.png", "texto": "O mascote da sala do Paleozoico, Trilobit, baseado nos trilobitas, um dos animais famosos do Paleozoico."},
        {"img": "anomalucaris.png", "texto": "Imagem de um dos maiores predadores do Paleozoico, o Anomalocaris."},
        {"img": "carbonifero2.jpg", "texto": "Imagem de uma floresta do período Carbonífero, onde se formaram grandes depósitos de carvão."},
        {"img": "meganeura.jpeg", "texto": "Imagem de uma libélula gigante do período Carbonífero, conhecida como Meganeura, com envergadura de até 70 cm."},
    ]},
    {"nome": "Mesozoico", "itens": [
        {"img": "KRW-T-Rex_Dopant.webp", "texto": "O mascote da sala do Mesozoico, Tony Rex, baseado no famoso dinossauro carnívoro Tyrannosaurus rex."},
        {"img": "irritator.png", "texto": "Imagem de um gênero de dinossauro espinossaurídeo que viveu no que hoje é o Brasil durante o estágio Albiano do Período Cretáceo Inferior."},
        {"img": "asteroide.png", "texto": "Imagem do asteroide que atingiu a península de Yucatán, no México, causando a extinção em massa do Cretáceo-Paleógeno."},
        {"img": "Fossil.jpeg", "texto": "Imagem de um fóssil de dinossauro que mostra a características de penas sendo uma grande descoberta."},
    ]},
    {"nome": "Cenozoico", "itens": [
        {"img": "mascotecaver.png", "texto": "O mascote da sala do Cenozoico, Caveson, baseado em um homem das cavernas, representando a evolução humana durante o período Cenozoico."},
        {"img": "biface.png", "texto": "Imagem de uma ferramenta de pedra lascada, representando a tecnologia utilizada pelos primeiros humanos durante o período Cenozoico."},
        {"img": "gigatatu.png", "texto": "Imagem de um gliptodonte, um dos animais famosos do Cenozoico que viveu na América do Sul."},
        {"img": "eradogelo.jpg", "texto": "Imagem representando a Era do Gelo, um período de clima frio que ocorreu durante o Pleistoceno, parte do Cenozoico."},
    ]},
]

credits = [
    ("Senhor Magzor e Tony Rex", "Imagens retiradas da série Kamen Rider W"),
    ("Caveson", "Feito por mim usando o programa LibreSprite"),
    ("Resto das imagens", "Foram retiradas do Wikimedia Commons e do Google Imagens, com licenças de uso livre ou fair use"),
    ("tilobits", "imagem retirada do jogo Mega Manx8"),
    ("imagem do meganeura", "imagem retirada da serie de supersentai ohsama sentai king ohger (2023)")
]


def abrir_sala(fase):
    sala = tk.Toplevel(hall)
    sala.title(fase["nome"])
    sala.geometry("550x550")
    
    itens = fase["itens"]
    posicao = [0]

    tk.Label(sala, text=fase["nome"], font=("Arial", 24, "bold")).pack(pady=10)
    
    lbl_img = tk.Label(sala, cursor="hand2")
    lbl_img.pack(pady=5)
    
    lbl_texto = tk.Label(sala, text="Clique na imagem para ler a descrição", wraplength=450, font=("Arial", 11, "italic"), fg="gray")
    lbl_texto.pack(pady=10)

    def mostrar():
        item = itens[posicao[0]]
        caminho_img = os.path.join(PASTA, item["img"])
        
        if os.path.exists(caminho_img):
            img = Image.open(caminho_img)
            img.thumbnail((500, 300))
            foto = ImageTk.PhotoImage(img)
            lbl_img.config(image=foto)
            lbl_img.image = foto
        else:
            lbl_img.config(image="", text=f"[Imagem não encontrada:\n{item['img']}]", font=("Arial", 12), fg="red")
            
        lbl_texto.config(text="Clique na imagem para ler a descrição", font=("Arial", 11, "italic"), fg="gray")

    def clica_imagem(evento):
        item = itens[posicao[0]]
        if lbl_texto.cget("text") == item["texto"]:
            lbl_texto.config(text="Clique na imagem para ler a descrição", font=("Arial", 11, "italic"), fg="gray")
        else:
            lbl_texto.config(text=item["texto"], font=("Arial", 12, "normal"), fg="black")

    def mudar(passo):
        posicao[0] = (posicao[0] + passo) % len(itens)
        mostrar()

    lbl_img.bind("<Button-1>", clica_imagem)
    
    frame_botoes = tk.Frame(sala)
    frame_botoes.pack(side="bottom", fill="x", pady=15)
    
    tk.Button(frame_botoes, text="← Anterior", font=("Arial", 10), command=lambda: mudar(-1)).pack(side="left", padx=30)
    tk.Button(frame_botoes, text="Voltar ao hall", font=("Arial", 10), command=sala.destroy).pass_side = tk.LEFT if hasattr(tk, 'LEFT') else tk.Button(frame_botoes, text="Voltar ao hall", font=("Arial", 10), command=sala.destroy).pack(side="left", expand=True) 
    tk.Button(frame_botoes, text="Próxima →", font=("Arial", 10), command=lambda: mudar(1)).pack(side="right", padx=30)

    mostrar()


def abrir_creditos():
    sala = tk.Toplevel(hall)
    sala.title("Créditos")
    sala.geometry("550x300")
    
    tk.Label(sala, text="Créditos das Imagens", font=("Arial", 18, "bold")).pack(pady=15)
    
    frame_lista = tk.Frame(sala)
    frame_lista.pack(padx=20, fill="both", expand=True)
    
    for imagem, fonte in credits:
        tk.Label(frame_lista, text=f"• {imagem}: {fonte}", wraplength=500, justify="left", font=("Arial", 10)).pack(anchor="w", pady=4)
        
    tk.Button(sala, text="Voltar ao hall", font=("Arial", 10), command=sala.destroy).pack(pady=15)



hall = tk.Tk()
hall.title("Museu Geológico")
hall.geometry("350x450")

tk.Label(hall, text="Bem-vindo ao\nMuseu Geológico!", font=("Arial", 18, "bold"), justify="center").pack(pady=15)



tk.Label(hall, text="Digite seu nome para começar:", font=("Arial", 10)).pack(pady=2)

entrada_nome = tk.Entry(hall, font=("Arial", 11), justify="center", width=25)
entrada_nome.pack(pady=5)

lbl_saudacao = tk.Label(hall, text="", font=("Arial", 10, "bold"), fg="blue")
lbl_saudacao.pack(pady=5)

def cumprimentar_visitante():
   
    nome_usuario = entrada_nome.get()
    
    if nome_usuario.strip() == "":
        lbl_saudacao.config(text="Por favor, digite seu nome!", fg="red")
    else:
        
        mensagem = f"Olá, {nome_usuario.title()}! Escolha uma sala:"
        lbl_saudacao.config(text=mensagem, fg="green")

tk.Button(hall, text="Salvar Nome", font=("Arial", 9), command=cumprimentar_visitante).pack(pady=2)

tk.Label(hall, text="Escolha uma sala para visitar:", font=("Arial", 11)).pack(pady=10)

for fase in fases:
    tk.Button(hall, text=f"Sala {fase['nome']}", width=25, font=("Arial", 10),
              command=lambda f=fase: abrir_sala(f)).pack(pady=4)

tk.Button(hall, text="Créditos", width=25, font=("Arial", 10, "italic"), command=abrir_creditos).pack(pady=10)

hall.mainloop()


     
     

    
       
      
    
    


                   
    