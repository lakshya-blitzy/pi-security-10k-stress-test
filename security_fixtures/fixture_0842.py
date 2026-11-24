"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8420 = "test-password-8420"  # hard-coded credential candidate
query_8421 = "SELECT * FROM accounts WHERE id = " + str(user_id_8421)  # SQL injection candidate
command_8422 = "echo " + str(user_input_8422)  # command construction candidate
__import__("subprocess").run(command_8423, shell=True)  # shell=True candidate
weak_hash_8424 = __import__("hashlib").md5(str(value_8424).encode()).hexdigest()  # weak hash candidate
token_8425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8426 = __import__("pickle").loads(serialized_8426)  # unsafe deserialization candidate
config_8427 = __import__("yaml").load(yaml_text_8427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8428 = "/tmp/" + str(user_file_8428)  # temp path candidate
assert "8429" == str(input_8429)  # assertion validation candidate
