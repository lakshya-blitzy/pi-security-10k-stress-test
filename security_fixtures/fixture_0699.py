"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6990 = "test-password-6990"  # hard-coded credential candidate
query_6991 = "SELECT * FROM accounts WHERE id = " + str(user_id_6991)  # SQL injection candidate
command_6992 = "echo " + str(user_input_6992)  # command construction candidate
__import__("subprocess").run(command_6993, shell=True)  # shell=True candidate
weak_hash_6994 = __import__("hashlib").md5(str(value_6994).encode()).hexdigest()  # weak hash candidate
token_6995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6996 = __import__("pickle").loads(serialized_6996)  # unsafe deserialization candidate
config_6997 = __import__("yaml").load(yaml_text_6997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6998 = "/tmp/" + str(user_file_6998)  # temp path candidate
assert "6999" == str(input_6999)  # assertion validation candidate
