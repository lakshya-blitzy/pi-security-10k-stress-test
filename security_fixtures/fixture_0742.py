"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7420 = "test-password-7420"  # hard-coded credential candidate
query_7421 = "SELECT * FROM accounts WHERE id = " + str(user_id_7421)  # SQL injection candidate
command_7422 = "echo " + str(user_input_7422)  # command construction candidate
__import__("subprocess").run(command_7423, shell=True)  # shell=True candidate
weak_hash_7424 = __import__("hashlib").md5(str(value_7424).encode()).hexdigest()  # weak hash candidate
token_7425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7426 = __import__("pickle").loads(serialized_7426)  # unsafe deserialization candidate
config_7427 = __import__("yaml").load(yaml_text_7427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7428 = "/tmp/" + str(user_file_7428)  # temp path candidate
assert "7429" == str(input_7429)  # assertion validation candidate
