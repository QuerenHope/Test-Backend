from .models import UploadCnabFile, UploadFileForm, Cnab
from django.shortcuts import render


def UploadCnabView(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"]

        CNAB_archive = UploadCnabFile.objects.create(file=file)

        CNAB_archive.save()

        file_list = []

        with open(f"./{str(CNAB_archive.file)}", "r", encoding="utf-8") as archive_file:
            for archiveCNAB in archive_file:
                file_list.append(archiveCNAB)

        for loop_arc_cnab in file_list:
            type = loop_arc_cnab[:1]
            ano = loop_arc_cnab[1:5]
            mes = loop_arc_cnab[5:7]
            dia = loop_arc_cnab[7:9]
            value = loop_arc_cnab[9:19]
            cpf: str = loop_arc_cnab[19:30]
            credit_card: str = loop_arc_cnab[30:42]
            hour_item = loop_arc_cnab[42:44]
            minuto = loop_arc_cnab[44:46]
            segundo = loop_arc_cnab[46:48]
            owner_shop: str = loop_arc_cnab[48:62]
            shop_name: str = loop_arc_cnab[62:81]
            cnab_file = loop_arc_cnab[81:91]

            date = f"{ano}-{mes}-{dia}"
            value = int(value) / 100
            hour = f"{hour_item}:{minuto}:{segundo}"

            if type == "1":
                type = "Débito"

            elif type == "2":
                type = "Boleto"

            elif type == "3":
                type = "Financiamento"

            elif type == "4":
                type = "Crédito"

            elif type == "5":
                type = "Recebimento Empréstimo"

            elif type == "6":
                type = "Vendas"

            elif type == "7":
                type = "Recebimento TED"

            elif type == "8":
                type = "Recebimento DOC"

            elif type == "9":
                type = "Aluguel"

            reader = Cnab.objects.create(
                type=type.strip(),
                date=date.strip(),
                value=value,
                cpf=cpf.strip(),
                credit_card=credit_card.strip(),
                hour=hour.strip(),
                owner_shop=owner_shop.strip(),
                shop_name=shop_name.strip(),
                cnab_file=cnab_file.strip(),
            )

            reader.save()

        transacoes = Cnab.objects.values(
            "type",
            "value",
            "date",
            "cpf",
            "credit_card",
            "hour",
            "owner_shop",
            "shop_name",
            "cnab_file",
        ).order_by("owner_shop")

        saldo_total_por_loja = {}

        for transacao in transacoes:
            if transacao["owner_shop"] not in saldo_total_por_loja:
                saldo_total_por_loja[transacao["owner_shop"]] = 0
            if (
                transacao["type"] == "Boleto"
                or transacao["type"] == "Financiamento"
                or transacao["type"] == "Aluguel"
            ):
                saldo_total_por_loja[transacao["owner_shop"]] -= transacao["value"]
            else:
                saldo_total_por_loja[transacao["owner_shop"]] += transacao["value"]

        return render(
            request,
            "results.html",
            context={
                "transacoes": transacoes,
                "saldo_total_por_loja": saldo_total_por_loja,
            },
        )

    else:
        form = UploadFileForm()
    return render(request, "home.html", {"form": form})
