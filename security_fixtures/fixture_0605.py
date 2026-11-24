"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6050 = "test-password-6050"  # hard-coded credential candidate
query_6051 = "SELECT * FROM accounts WHERE id = " + str(user_id_6051)  # SQL injection candidate
command_6052 = "echo " + str(user_input_6052)  # command construction candidate
__import__("subprocess").run(command_6053, shell=True)  # shell=True candidate
weak_hash_6054 = __import__("hashlib").md5(str(value_6054).encode()).hexdigest()  # weak hash candidate
token_6055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6056 = __import__("pickle").loads(serialized_6056)  # unsafe deserialization candidate
config_6057 = __import__("yaml").load(yaml_text_6057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6058 = "/tmp/" + str(user_file_6058)  # temp path candidate
assert "6059" == str(input_6059)  # assertion validation candidate
