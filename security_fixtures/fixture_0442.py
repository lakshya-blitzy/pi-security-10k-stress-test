"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4420 = "test-password-4420"  # hard-coded credential candidate
query_4421 = "SELECT * FROM accounts WHERE id = " + str(user_id_4421)  # SQL injection candidate
command_4422 = "echo " + str(user_input_4422)  # command construction candidate
__import__("subprocess").run(command_4423, shell=True)  # shell=True candidate
weak_hash_4424 = __import__("hashlib").md5(str(value_4424).encode()).hexdigest()  # weak hash candidate
token_4425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4426 = __import__("pickle").loads(serialized_4426)  # unsafe deserialization candidate
config_4427 = __import__("yaml").load(yaml_text_4427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4428 = "/tmp/" + str(user_file_4428)  # temp path candidate
assert "4429" == str(input_4429)  # assertion validation candidate
