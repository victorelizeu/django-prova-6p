from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncMonth


def calcular_metricas(base_qs):
    kpis = base_qs.annotate(
        qtd_comentarios=Count("comentarios")
    ).aggregate(
        total_posts=Count("id"),
        publicados=Count("id", filter=Q(estados="Publicado")),
        em_revisao=Count("id", filter=Q(estados="Em_Revisao")),
        total_comentarios=Sum("qtd_comentarios"),
    )
    kpis["total_comentarios"] = kpis["total_comentarios"] or 0

    ranking_autores = (
        base_qs.values("autor__usuario__username")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )

    por_categoria = (
        base_qs.values("categoria__nome")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    por_mes_qs = (
        base_qs.annotate(mes=TruncMonth("data"))
        .values("mes")
        .annotate(total=Count("id"))
        .order_by("mes")
    )
    por_mes = [
        {"mes": r["mes"].strftime("%m/%Y"), "total": r["total"]}
        for r in por_mes_qs
        if r["mes"] is not None
    ]

    return {
        "kpis": kpis,
        "ranking_autores": ranking_autores,
        "por_categoria": por_categoria,
        "por_mes": por_mes,
    }
