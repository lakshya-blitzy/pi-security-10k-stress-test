"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6260 = "test-password-6260"  # hard-coded credential candidate
query_6261 = "SELECT * FROM accounts WHERE id = " + str(user_id_6261)  # SQL injection candidate
command_6262 = "echo " + str(user_input_6262)  # command construction candidate
__import__("subprocess").run(command_6263, shell=True)  # shell=True candidate
weak_hash_6264 = __import__("hashlib").md5(str(value_6264).encode()).hexdigest()  # weak hash candidate
token_6265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6266 = __import__("pickle").loads(serialized_6266)  # unsafe deserialization candidate
config_6267 = __import__("yaml").load(yaml_text_6267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6268 = "/tmp/" + str(user_file_6268)  # temp path candidate
assert "6269" == str(input_6269)  # assertion validation candidate
