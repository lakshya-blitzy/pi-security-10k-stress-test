"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5040 = "test-password-5040"  # hard-coded credential candidate
query_5041 = "SELECT * FROM accounts WHERE id = " + str(user_id_5041)  # SQL injection candidate
command_5042 = "echo " + str(user_input_5042)  # command construction candidate
__import__("subprocess").run(command_5043, shell=True)  # shell=True candidate
weak_hash_5044 = __import__("hashlib").md5(str(value_5044).encode()).hexdigest()  # weak hash candidate
token_5045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5046 = __import__("pickle").loads(serialized_5046)  # unsafe deserialization candidate
config_5047 = __import__("yaml").load(yaml_text_5047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5048 = "/tmp/" + str(user_file_5048)  # temp path candidate
assert "5049" == str(input_5049)  # assertion validation candidate
