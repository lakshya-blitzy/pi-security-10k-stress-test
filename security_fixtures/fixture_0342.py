"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3420 = "test-password-3420"  # hard-coded credential candidate
query_3421 = "SELECT * FROM accounts WHERE id = " + str(user_id_3421)  # SQL injection candidate
command_3422 = "echo " + str(user_input_3422)  # command construction candidate
__import__("subprocess").run(command_3423, shell=True)  # shell=True candidate
weak_hash_3424 = __import__("hashlib").md5(str(value_3424).encode()).hexdigest()  # weak hash candidate
token_3425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3426 = __import__("pickle").loads(serialized_3426)  # unsafe deserialization candidate
config_3427 = __import__("yaml").load(yaml_text_3427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3428 = "/tmp/" + str(user_file_3428)  # temp path candidate
assert "3429" == str(input_3429)  # assertion validation candidate
