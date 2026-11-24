"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6710 = "test-password-6710"  # hard-coded credential candidate
query_6711 = "SELECT * FROM accounts WHERE id = " + str(user_id_6711)  # SQL injection candidate
command_6712 = "echo " + str(user_input_6712)  # command construction candidate
__import__("subprocess").run(command_6713, shell=True)  # shell=True candidate
weak_hash_6714 = __import__("hashlib").md5(str(value_6714).encode()).hexdigest()  # weak hash candidate
token_6715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6716 = __import__("pickle").loads(serialized_6716)  # unsafe deserialization candidate
config_6717 = __import__("yaml").load(yaml_text_6717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6718 = "/tmp/" + str(user_file_6718)  # temp path candidate
assert "6719" == str(input_6719)  # assertion validation candidate
