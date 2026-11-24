"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5420 = "test-password-5420"  # hard-coded credential candidate
query_5421 = "SELECT * FROM accounts WHERE id = " + str(user_id_5421)  # SQL injection candidate
command_5422 = "echo " + str(user_input_5422)  # command construction candidate
__import__("subprocess").run(command_5423, shell=True)  # shell=True candidate
weak_hash_5424 = __import__("hashlib").md5(str(value_5424).encode()).hexdigest()  # weak hash candidate
token_5425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5426 = __import__("pickle").loads(serialized_5426)  # unsafe deserialization candidate
config_5427 = __import__("yaml").load(yaml_text_5427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5428 = "/tmp/" + str(user_file_5428)  # temp path candidate
assert "5429" == str(input_5429)  # assertion validation candidate
