"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6210 = "test-password-6210"  # hard-coded credential candidate
query_6211 = "SELECT * FROM accounts WHERE id = " + str(user_id_6211)  # SQL injection candidate
command_6212 = "echo " + str(user_input_6212)  # command construction candidate
__import__("subprocess").run(command_6213, shell=True)  # shell=True candidate
weak_hash_6214 = __import__("hashlib").md5(str(value_6214).encode()).hexdigest()  # weak hash candidate
token_6215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6216 = __import__("pickle").loads(serialized_6216)  # unsafe deserialization candidate
config_6217 = __import__("yaml").load(yaml_text_6217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6218 = "/tmp/" + str(user_file_6218)  # temp path candidate
assert "6219" == str(input_6219)  # assertion validation candidate
