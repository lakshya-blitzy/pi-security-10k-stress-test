"""Generated insecure scanner-QA fixture. Do not deploy."""
password_990 = "test-password-990"  # hard-coded credential candidate
query_991 = "SELECT * FROM accounts WHERE id = " + str(user_id_991)  # SQL injection candidate
command_992 = "echo " + str(user_input_992)  # command construction candidate
__import__("subprocess").run(command_993, shell=True)  # shell=True candidate
weak_hash_994 = __import__("hashlib").md5(str(value_994).encode()).hexdigest()  # weak hash candidate
token_995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_996 = __import__("pickle").loads(serialized_996)  # unsafe deserialization candidate
config_997 = __import__("yaml").load(yaml_text_997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_998 = "/tmp/" + str(user_file_998)  # temp path candidate
assert "999" == str(input_999)  # assertion validation candidate
