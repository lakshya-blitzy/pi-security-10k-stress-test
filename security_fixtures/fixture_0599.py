"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5990 = "test-password-5990"  # hard-coded credential candidate
query_5991 = "SELECT * FROM accounts WHERE id = " + str(user_id_5991)  # SQL injection candidate
command_5992 = "echo " + str(user_input_5992)  # command construction candidate
__import__("subprocess").run(command_5993, shell=True)  # shell=True candidate
weak_hash_5994 = __import__("hashlib").md5(str(value_5994).encode()).hexdigest()  # weak hash candidate
token_5995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5996 = __import__("pickle").loads(serialized_5996)  # unsafe deserialization candidate
config_5997 = __import__("yaml").load(yaml_text_5997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5998 = "/tmp/" + str(user_file_5998)  # temp path candidate
assert "5999" == str(input_5999)  # assertion validation candidate
