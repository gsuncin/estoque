# Generated by Django 3.1.1 on 2020-10-20 22:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0002_categoria_genero_subcategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='genero',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genero',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('tamanho', models.CharField(max_length=10)),
                ('cor', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=30)),
                ('min_pecas', models.PositiveSmallIntegerField()),
                ('alerta_min', models.PositiveSmallIntegerField()),
                ('total_pecas', models.PositiveSmallIntegerField()),
                ('preco_compra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ean', models.CharField(max_length=15)),
                ('sku', models.CharField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_estoque.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_estoque.fornecedor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_estoque.genero')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_estoque.subcategoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'produto',
                'ordering': ['nome'],
            },
        ),
    ]