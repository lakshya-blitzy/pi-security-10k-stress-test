"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3040 = "test-password-3040"  # hard-coded credential candidate
query_3041 = "SELECT * FROM accounts WHERE id = " + str(user_id_3041)  # SQL injection candidate
command_3042 = "echo " + str(user_input_3042)  # command construction candidate
__import__("subprocess").run(command_3043, shell=True)  # shell=True candidate
weak_hash_3044 = __import__("hashlib").md5(str(value_3044).encode()).hexdigest()  # weak hash candidate
token_3045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3046 = __import__("pickle").loads(serialized_3046)  # unsafe deserialization candidate
config_3047 = __import__("yaml").load(yaml_text_3047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3048 = "/tmp/" + str(user_file_3048)  # temp path candidate
assert "3049" == str(input_3049)  # assertion validation candidate
