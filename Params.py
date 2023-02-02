import argparse

def ParseArgs():
	parser = argparse.ArgumentParser(description='Model Params')
	parser.add_argument('--lr', default=1e-3, type=float, help='learning rate')
	parser.add_argument('--batch', default=4096, type=int, help='batch size')
	parser.add_argument('--tstBat', default=256, type=int, help='number of users in a testing batch')
	parser.add_argument('--reg', default=1e-5, type=float, help='weight decay regularizer')
	parser.add_argument('--epoch', default=200, type=int, help='number of epochs')
	parser.add_argument('--save_path', default='tem', help='file name to save model and training record')
	parser.add_argument('--latdim', default=32, type=int, help='embedding size')
	parser.add_argument('--gnn_layer', default=2, type=int, help='number of gnn layers')
	parser.add_argument('--topk', default=20, type=int, help='K of top K')
	parser.add_argument('--data', default='yelp', type=str, help='name of dataset')
	parser.add_argument('--ssl_reg', default=0.1, type=float, help='weight for contrative learning')
	parser.add_argument('--temp', default=0.5, type=float, help='temperature in contrastive learning')
	parser.add_argument('--tstEpoch', default=1, type=int, help='number of epoch to test while training')
	parser.add_argument('--gpu', default=-1, type=int, help='indicates which gpu to use')

	parser.add_argument('--lambda1', type=float, default=0.01, help='Weight for L0 loss on laplacian matrix.')

	parser.add_argument('--gamma', type=float, default=-0.45)
	parser.add_argument('--zeta', type=float, default=1.05)
	parser.add_argument('--init_temperature', type=float, default=2.0)
	parser.add_argument('--temperature_decay', type=float, default=0.98)

	parser.add_argument("--eps", type=float, default=1e-8)
	parser.add_argument("--ssl_bpr_reg", type=float, default=1)
	parser.add_argument("--ib_reg", type=float, default=0.1)

	parser.add_argument("--seed", type=int, default=421, help="random seed")
	
	return parser.parse_args()
args = ParseArgs()