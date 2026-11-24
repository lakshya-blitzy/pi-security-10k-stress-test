"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8990 = "test-password-8990"  # hard-coded credential candidate
query_8991 = "SELECT * FROM accounts WHERE id = " + str(user_id_8991)  # SQL injection candidate
command_8992 = "echo " + str(user_input_8992)  # command construction candidate
__import__("subprocess").run(command_8993, shell=True)  # shell=True candidate
weak_hash_8994 = __import__("hashlib").md5(str(value_8994).encode()).hexdigest()  # weak hash candidate
token_8995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8996 = __import__("pickle").loads(serialized_8996)  # unsafe deserialization candidate
config_8997 = __import__("yaml").load(yaml_text_8997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8998 = "/tmp/" + str(user_file_8998)  # temp path candidate
assert "8999" == str(input_8999)  # assertion validation candidate
