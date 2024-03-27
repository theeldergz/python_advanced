import logging

root_logger = logging.getLogger('root_logger')
logging.basicConfig()
root_logger.setLevel('DEBUG')
sub_1 = logging.getLogger('root_logger.sub_1')
sub_2 = logging.getLogger('root_logger.sub_2')
sub_sub_1 = logging.getLogger('root_logger.sub_1.sub_sub_1')

lvl_handler = logging.StreamHandler()
lvl_handler.setLevel('DEBUG')

sub_1.setLevel('DEBUG')
sub_1.addHandler(lvl_handler)
sub_sub_1.setLevel('DEBUG')

formatter = logging.Formatter(fmt='%(name)s || %(levelname)s || %(message)s')

lvl_handler.setFormatter(formatter)

print(
    root_logger, root_logger.handlers,
    '\n\t', sub_1, sub_1.handlers,
    '\n\t', sub_2, sub_2.handlers,
    '\n\t\t', sub_sub_1, sub_sub_1.handlers
)

print(
    sub_1.debug('test sub1'),
    sub_2.debug('test sub2'),
    sub_sub_1.debug('test subsub')
)
