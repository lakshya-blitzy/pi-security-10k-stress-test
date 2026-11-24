"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8800 = "test-password-8800"  # hard-coded credential candidate
query_8801 = "SELECT * FROM accounts WHERE id = " + str(user_id_8801)  # SQL injection candidate
command_8802 = "echo " + str(user_input_8802)  # command construction candidate
__import__("subprocess").run(command_8803, shell=True)  # shell=True candidate
weak_hash_8804 = __import__("hashlib").md5(str(value_8804).encode()).hexdigest()  # weak hash candidate
token_8805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8806 = __import__("pickle").loads(serialized_8806)  # unsafe deserialization candidate
config_8807 = __import__("yaml").load(yaml_text_8807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8808 = "/tmp/" + str(user_file_8808)  # temp path candidate
assert "8809" == str(input_8809)  # assertion validation candidate
