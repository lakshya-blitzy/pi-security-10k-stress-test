"""Generated insecure scanner-QA fixture. Do not deploy."""
password_200 = "test-password-200"  # hard-coded credential candidate
query_201 = "SELECT * FROM accounts WHERE id = " + str(user_id_201)  # SQL injection candidate
command_202 = "echo " + str(user_input_202)  # command construction candidate
__import__("subprocess").run(command_203, shell=True)  # shell=True candidate
weak_hash_204 = __import__("hashlib").md5(str(value_204).encode()).hexdigest()  # weak hash candidate
token_205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_206 = __import__("pickle").loads(serialized_206)  # unsafe deserialization candidate
config_207 = __import__("yaml").load(yaml_text_207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_208 = "/tmp/" + str(user_file_208)  # temp path candidate
assert "209" == str(input_209)  # assertion validation candidate
