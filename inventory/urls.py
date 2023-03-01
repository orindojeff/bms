from django.urls import path
from .views import (
    index,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderListView,
    SalesCreateView,
    SalesUpdateView,
    SalesDeleteView,
    SalesListView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    PaymentListView,
    OrderPDFView,
    OrderXLSView,
    OrderDocsView,
    PaymentPDFView,
    PaymentXLSView,
    PaymentdocxView,
    SalesPDFView,
    SalesXlsView,
    SaleDocsView,
)



app_name = 'inventory'

urlpatterns = [
    path('', index, name='index'),
    # Order URLs
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/', OrderListView.as_view(), name='order-list'),

    # Sales URLs
    path('sales/create/', SalesCreateView.as_view(), name='sales-create'),
    path('sales/<int:pk>/update/', SalesUpdateView.as_view(), name='sales-update'),
    path('sales/<int:pk>/delete/', SalesDeleteView.as_view(), name='sales-delete'),
    path('sales/', SalesListView.as_view(), name='sales-list'),

    # Payment URLs
    path('payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),


    # export functions urls
    # path('export/csv/', OrderCSVView.as_view(), name='order_export_csv'),
    path('export/pdf/', OrderPDFView.as_view(), name='order-pdf'),
    path('export/xls/', OrderXLSView.as_view(), name='order-xls'),
    path('export/docs/', OrderDocsView.as_view(), name='order-docs'),
    # path('payment/list/csv/', PaymentListCSVView.as_view(), name='payment_csv_list'),
    path('payment/list/pdf/', PaymentPDFView.as_view(), name='payment_pdf_list'),
    path('payment/list/xls/', PaymentXLSView.as_view(), name='payment_xls_list'),
    path('payment/list/docx/', PaymentdocxView.as_view(), name='payment_docx_list'),
    path('sales/pdf/', SalesPDFView.as_view(), name='sales_pdf'),
    path('sales/xls/', SalesXlsView.as_view(), name='sales_xls'),
    path('sales/docs/', SaleDocsView.as_view(), name='sales_docs'),
]
