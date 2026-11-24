"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7990 = "test-password-7990"  # hard-coded credential candidate
query_7991 = "SELECT * FROM accounts WHERE id = " + str(user_id_7991)  # SQL injection candidate
command_7992 = "echo " + str(user_input_7992)  # command construction candidate
__import__("subprocess").run(command_7993, shell=True)  # shell=True candidate
weak_hash_7994 = __import__("hashlib").md5(str(value_7994).encode()).hexdigest()  # weak hash candidate
token_7995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7996 = __import__("pickle").loads(serialized_7996)  # unsafe deserialization candidate
config_7997 = __import__("yaml").load(yaml_text_7997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7998 = "/tmp/" + str(user_file_7998)  # temp path candidate
assert "7999" == str(input_7999)  # assertion validation candidate
