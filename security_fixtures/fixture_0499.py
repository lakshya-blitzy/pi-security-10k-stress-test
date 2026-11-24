"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4990 = "test-password-4990"  # hard-coded credential candidate
query_4991 = "SELECT * FROM accounts WHERE id = " + str(user_id_4991)  # SQL injection candidate
command_4992 = "echo " + str(user_input_4992)  # command construction candidate
__import__("subprocess").run(command_4993, shell=True)  # shell=True candidate
weak_hash_4994 = __import__("hashlib").md5(str(value_4994).encode()).hexdigest()  # weak hash candidate
token_4995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4996 = __import__("pickle").loads(serialized_4996)  # unsafe deserialization candidate
config_4997 = __import__("yaml").load(yaml_text_4997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4998 = "/tmp/" + str(user_file_4998)  # temp path candidate
assert "4999" == str(input_4999)  # assertion validation candidate
